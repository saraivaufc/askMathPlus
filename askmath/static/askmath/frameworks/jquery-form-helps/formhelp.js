(function($) {
    $.formHelp = function(options /**/, disableTimer /*Internal use*/){     
        disableTimer = (disableTimer === undefined ? false : disableTimer);
        options = $.extend({}, {pushpinEnabled: false}, options);
        
        $('span.'+(options.classPrefix ? options.classPrefix+'-helptext' : 'helptext')).each(function(){
            
            // Grab the inputelement(s) for this helpbox
            var inputelements = $(this).attr('data-for');   
            inputelements = inputelements.replace("\\", "");
            var $inputelements = $(inputelements);
                        
            var $helpbox = $('<div/>')
                    .addClass(options && options.classPrefix ? options.classPrefix+'-form-helpbox' : 'form-helpbox')
                    .attr('data-for', inputelements)
                    .css('z-index', 99999999)
                    .data('pushpinned', false)
                    .append($('<div/>')
                    .addClass('content')
                    .html('<div class="tools"><img class="pushpin" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAB9JREFUeNpi/P//PwMlgImBQjBqwKgBowYMFgMAAgwAY5oDHVti48YAAAAASUVORK5CYII=" /></div>'+$(this).html()));

            $('body').prepend($helpbox);
            
            if (options.pushpinEnabled) {
                $helpbox.find('.tools').show();
            }
            
            // Handle pushpin actions
            $helpbox.find('.pushpin').on('mousedown', function(){
                $helpbox.data('pushpinned', !$helpbox.data('pushpinned'));
            }).on('mouseup', function(){
                if ($helpbox.data('pushpinned')) {
                    $(this).addClass('pinned');
                } else {
                    $(this).removeClass('pinned');
                    $helpbox.fadeOut('fast');
                }
                
            });
            
            // Collect elements for calculating position of $helpbox
            var $boundaryElements = $inputelements;
            $inputelements.each(function(){
                $boundaryElements = $boundaryElements.add('label[for="'+$(this).attr('id')+'"]');
            });

            // Calculate top right corner of $boundaryElements and use
            // that value for the position of $helpbox
            var helpboxLeft = 0;
            var helpboxTop = $(document).height();
            $boundaryElements.each(function(){
                var thisLeft = $(this).offset().left + $(this).width();
                var thisTop = $(this).offset().top;
                helpboxLeft =  thisLeft > helpboxLeft ? thisLeft : helpboxLeft;
                helpboxTop = thisTop < helpboxTop ? thisTop : helpboxTop;
            });

            $inputelements.on('focus focusin', function(){
                $helpbox.css({
                    'left': helpboxLeft,
                    'top': helpboxTop
                }).fadeIn('fast');
            });

            $inputelements.on('blur focusout', function(){  
              if (!$helpbox.data('pushpinned')) {
                  $helpbox.fadeOut('fast');
              }
            });

            // There is no textarea resize event so we have to use mousemove            
            $inputelements.filter('textarea').on('mousemove', function(){
                $helpbox.css({
                    'left': $(this).offset().left + $(this).width(),
                    'top': $(this).offset().top
                });
            });
            
            // The elements that can't be clicked without changing their value or causing 
            // some kind of action. We use the mouseover/mouseout events instead of focus/blur.
            // The focus/blur events are still handled on these element because of the tab key.
            $inputelements.filter('[type="reset"],[type="submit"],[type="checkbox"],[type="radio"],[type="button"],[type="file"],[type="color"],[type="image"],[type="range"]').on('mouseover', function(){
                $(':input').blur();
                $helpbox.css({
                    'left': helpboxLeft,
                    'top': helpboxTop
                }).fadeIn('fast');             
            }).on('mouseout', function(){
                if (disableTimer) { //For QUnit testing purposes
                     if (!$helpbox.data('pushpinned')) {
                      $helpbox.fadeOut('fast');
                   } 
                } else {
                  setTimeout(function(){
                    if (!$helpbox.data('pushpinned')) {
                        $helpbox.fadeOut('fast');
                     } 
                  }, 1500);  
                }
                
                
            });
            
            $(this).remove();
        });

    };

}(jQuery));