$(function(){
	var alert_success = $("#alert-success");
	var alert_danger = $("#alert-danger");
	var alert_warning = $("#alert-warning");
	var alert_info = $("#alert-info");
	try{
		if(alert_success.length) {
			$.Notify({
			    caption: 'Success',
			    content: alert_success.val(),
			    type: 'success',
			});
		};
		if(alert_danger.length) {
			$.Notify({
			    caption: 'Alert',
			    content: alert_danger.val(),
			    type: 'alert',
			});
		};
		if (alert_warning.length) {
			$.Notify({
			    caption: 'Warning',
			    content: alert_warning.val(),
			    type: 'warning',
			});	
		};
	
		if(alert_info.length) {
			$.Notify({
			    caption: 'Info',
			    content: alert_info.val(),
			    type: 'info',
			});	
		}
	}catch(e){
		console.log("Erro alerts");
	}	
	
});