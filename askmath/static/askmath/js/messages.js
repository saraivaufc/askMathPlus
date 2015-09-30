$(function(){
	$("ul.messages > li.message").each(function(){
		noty({
		    text: $(this).text(),
		    theme: 'relax',
		    type: $(this).attr("value"),
		    animation: {
		        open: 'animated fadeInLeft', // Animate.css class names
		        close: 'animated flipOutX', // Animate.css class names
		    }
		});
	});
	
});