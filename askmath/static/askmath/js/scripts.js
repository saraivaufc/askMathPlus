function Init(){
	resize_window();
};

window.onresize = resize_window();

function resize_window(){
	var screean = parseInt($(window).height());
	var header = parseInt($("#header").css("height"));
	var main = parseInt($("#main").css("height"));
	var footer = parseInt($("#footer").css("height"));
	if ( (header + main + footer) < screean){
		var res = screean - header - footer;
		parseInt($("#main").css("height", (res-20) + "px"));
	};
}



$('#openBtn').click(function(){
	$('#myModal').modal({show:true})
});



$(function () {
    $('.button-checkbox').each(function () {

        // Settings
        var $widget = $(this),
            $button = $widget.find('button'),
            $checkbox = $widget.find('input:checkbox'),
            color = $button.data('color'),
            settings = {
                on: {
                    icon: 'glyphicon glyphicon-check'
                },
                off: {
                    icon: 'glyphicon glyphicon-unchecked'
                }
            };

        // Event Handlers
        $button.on('click', function () {
            $checkbox.prop('checked', !$checkbox.is(':checked'));
            $checkbox.triggerHandler('change');
            updateDisplay();
        });
        $checkbox.on('change', function () {
            updateDisplay();
        });

        // Actions
        function updateDisplay() {
            var isChecked = $checkbox.is(':checked');

            // Set the button's state
            $button.data('state', (isChecked) ? "on" : "off");

            // Set the button's icon
            $button.find('.state-icon')
                .removeClass()
                .addClass('state-icon ' + settings[$button.data('state')].icon);

            // Update the button's color
            if (isChecked) {
                $button
                    .removeClass('btn-default')
                    .addClass('btn-' + color + ' active');
            }
            else {
                $button
                    .removeClass('btn-' + color + ' active')
                    .addClass('btn-default');
            }
        }

        // Initialization
        function init() {

            updateDisplay();

            // Inject the icon if applicable
            if ($button.find('.state-icon').length == 0) {
                $button.prepend('<i class="state-icon ' + settings[$button.data('state')].icon + '"></i>');
            }
        }
        init();
    });
});

$("[type=file]").on("change", function(){
	// Name of file and placeholder
	var file = this.files[0].name;
	var dflt = $(this).attr("placeholder");
	if($(this).val()!=""){
		$(this).next().text(file);
	} else {
		$(this).next().text(dflt);
	}
});

function updateURLQuantityItems(){
	var form = $("#form_quantity_items");
	var quant = form.find("input[name='quantity_items']").val();
	var url =form.attr("action").concat("quantity_items=").concat(quant).concat("/");
	window.location = url;
	return false;
};


$(function(){
	$("#list_questions_sort").sortable();
	$("#list_videos_sort").sortable();
});

function sleep(ms) {
    var unixtime_ms = new Date().getTime();
    while(new Date().getTime() < unixtime_ms + ms) {}
}

function sortQuestions(){
	var list = $("#list_questions_sort");
	var order = [];
	list.find(".list").each(function(){
		try{
			order.push(parseInt($(this).attr("value")));
		}catch (e) {
			alert("Error sort questions!!!");
		}
	});
	var url = window.location.href;
	data = new Object();
	data['new_order'] = JSON.stringify(order);
	data['csrfmiddlewaretoken'] = $("input[name='csrfmiddlewaretoken']").val();
	$.post(url, data, function(data){
		$.Notify({
		    caption: 'Success',
		    content: "Questions Sorted Success!!!",
		    type: 'success',
		});
	});
};

function sortVideos(){
	var list = $("#list_videos_sort");
	var order = [];
	list.find(".list").each(function(){
		try{
			order.push(parseInt($(this).attr("value")));
		}catch (e) {
			$.Notify({
			    caption: 'Error',
			    content: "Erro sort videos!!!",
			    type: 'danger',
			});
		}
	});
	var url = window.location.href;
	data = new Object();
	data['new_order'] = JSON.stringify(order);
	data['csrfmiddlewaretoken'] = $("input[name='csrfmiddlewaretoken']").val();
	$.post(url, data, function(data){
		$.Notify({
		    caption: 'Success',
		    content: "Videos Sorted Success!!!",
		    type: 'success',
		});
	});
};

function help(){
	var url_help = $("input[name='url_help']").val();
	try {
		$.get(url_help, function(data){
		});
	} catch (e) {
		console.log(e);
	}
};

$(function(){
	$(".latex").each(function(){
		$(this).keyup(function(){
			Preview.Update();
		});
	});
});
	
$("#btn-help").click(help);

$(function(){
	$(".latex").focus(function(){
		var id = $(this).attr("id");
		$('#box-latex').attr('value',id);
		$("#latex_formula").val($(this).val());
		$('#box-latex').modal();
	});
	
	$("#latex_formula").keyup(function(){
		var latex = document.getElementById("latex_formula").value;
		var result = document.getElementById("MathPreview");
		typejax.updater.init(latex, latex.length, result);
	});
	
	$("#box-latex-submit").click(function(){
		var text = $("#latex_formula").val();
		$("#latex_formula").val("");
		var input_form = $("#" + $('#box-latex').attr('value'));
		input_form.text(text);
		$('#box-latex').modal('hide');
	});
});

$(function(){
	$("#select-signup").change(function(){
		if($(this).val() != "STUDENT"){
			$("#input-key").removeAttr("disabled");
			$("#input-key").attr("required","required");
		}else{
			$("#input-key").removeAttr("required");
			$("#input-key").attr("disabled", "disabled");
		}
	});
});