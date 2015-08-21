$(function(){
	var alerts = {};
	var alert_type= null;
	
	var alert_success = $("#alert-success");
	if (alert_success.length){
		alerts[alert_success.val()] = 'success';
	}	
	var alert_danger = $("#alert-danger");
	if (alert_danger.length){
		alerts[alert_danger.val()]= 'error';
	}
	var alert_info = $("#alert-info");
	if (alert_info.length){
		alerts[alert_info.val()] = 'information';
	}
	var alert_warning = $("#alert-warning");
	if (alert_warning.length){
		alerts[alert_warning.val()] = 'warning';
	}
	for(var x in alerts){
		noty({
		    text: x,
		    theme: 'relax',
		    type: alerts[x],
		    animation: {
		        open: 'animated fadeInLeft', // Animate.css class names
		        close: 'animated flipOutX', // Animate.css class names
		    }
		});
	}
	
});