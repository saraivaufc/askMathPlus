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



//QUESTION
$("input[name='radio_question']").change(function(){
	if($(this).prop( "checked", true ) ){
		var url_edit = "/home/manager/questions/edit/question=" + $(this).attr('question_id') + "/lesson="+ $(this).attr('lesson_id') +"/discipline=" + $(this).attr('discipline_id') + "/";
		var url_delete = "/home/manager/questions/remove/question=" + $(this).attr('question_id') + "/lesson="+ $(this).attr('lesson_id') +"/discipline="  + $(this).attr('discipline_id') + "/";
		var url_restore = "/home/manager/questions/restore/question=" + $(this).attr('question_id') + "/lesson="+ $(this).attr('lesson_id') +"/discipline="  + $(this).attr('discipline_id') + "/";
	}else{
		var url_edit = "#";
		var url_delete = "#";
		var url_restore = "#";
	};
	$("#button-question-edit").attr("href",url_edit);
	$("#button-question-delete").attr("href",url_delete);
	$("#button-question-restore").attr("href",url_restore);
});


//VIDEO
$("input[name='radio_video']").change(function(){
	if($(this).prop( "checked", true ) ){
		var url_edit = "/home/manager/videos/edit/video=" + $(this).attr('video_id') + "/lesson="+ $(this).attr('lesson_id') +"/discipline=" + $(this).attr('discipline_id') + "/";
		var url_delete = "/home/manager/videos/remove/video=" + $(this).attr('video_id') + "/lesson="+ $(this).attr('lesson_id') +"/discipline="  + $(this).attr('discipline_id') + "/";
		var url_restore = "/home/manager/videos/restore/video=" + $(this).attr('video_id') + "/lesson="+ $(this).attr('lesson_id') +"/discipline="  + $(this).attr('discipline_id') + "/";
	}else{
		var url_edit = "#";
		var url_delete = "#";
		var url_restore = "#";
	};
	$("#button-video-edit").attr("href",url_edit);
	$("#button-video-delete").attr("href",url_delete);
	$("#button-video-restore").attr("href",url_restore);
});