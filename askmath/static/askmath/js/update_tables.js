//DISCIPLINE
$("input[name='radio_discipline']").change(function(){
	if($(this).prop( "checked", true ) ){
		var url_edit = "/home/manager/disciplines/edit/discipline=" + $(this).attr('discipline_id') + "/";
		var url_delete = "/home/manager/disciplines/remove/discipline=" + $(this).attr('discipline_id') + "/";
		var url_restore = "/home/manager/disciplines/restore/discipline=" + $(this).attr('discipline_id') + "/";
	}else{
		var url_edit = "#";
		var url_delete = "#";
		var url_restore = "#";
	};
	$("#button-discipline-edit").attr("href",url_edit);
	$("#button-discipline-delete").attr("href",url_delete);
	$("#button-discipline-restore").attr("href",url_restore);
});


//LESSON
$("input[name='radio_lesson']").change(function(){
	if($(this).prop( "checked", true ) ){
		var url_edit = "/home/manager/lessons/edit/lesson="+ $(this).attr('lesson_id') +"/discipline=" + $(this).attr('discipline_id') + "/";
		var url_delete = "/home/manager/lessons/remove/lesson="+ $(this).attr('lesson_id') +"/discipline="  + $(this).attr('discipline_id') + "/";
		var url_restore = "/home/manager/lessons/restore/lesson="+ $(this).attr('lesson_id') +"/discipline="  + $(this).attr('discipline_id') + "/";
	}else{
		var url_edit = "#";
		var url_delete = "#";
		var url_restore = "#";
	};
	$("#button-lesson-edit").attr("href",url_edit);
	$("#button-lesson-delete").attr("href",url_delete);
	$("#button-lesson-restore").attr("href",url_restore);
});