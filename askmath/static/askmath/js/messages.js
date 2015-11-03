$(function(){
	$("ul.messages > li.message").each(function(){
		noty({
		    text: $(this).text(),
		    theme: 'relax',
		    type: $(this).attr("value"),
		    animation: {
		        open: 'animated bounceInUp', // Animate.css class names
		        close: 'animated bounceOutDown', // Animate.css class names
		    }
		});
	});
	
});