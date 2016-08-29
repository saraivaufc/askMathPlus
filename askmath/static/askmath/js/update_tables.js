$(function () {
	$('.dataTable').each(function(){
		var table = $(this). dataTable({
			"language": {
				"url": "/static/askmath/frameworks/jquery/i18n/Portuguese-Brasil.json"
			},
			"paging":   false,
		      "ordering": false,
		      "info": false,
		});
	});
});


//CLASSE
$("input[name='radio_classe']").change(function(){
	if($(this).prop( "checked", true ) ){
		var url_edit = "/home/manager/classes/edit/classe=" + $(this).attr('classe_id') + "/";
		var url_delete = "/home/manager/classes/remove/classe=" + $(this).attr('classe_id') + "/";
		var url_restore = "/home/manager/classes/restore/classe=" + $(this).attr('classe_id') + "/";
	}else{
		var url_edit = "#";
		var url_delete = "#";
		var url_restore = "#";
	};
	$("#button-classe-edit").attr("href",url_edit);
	$("#button-classe-delete").attr("href",url_delete);
	$("#button-classe-restore").attr("href",url_restore);
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

//CATEGORY
$("input[name='radio_category']").change(function(){
	if($(this).prop( "checked", true ) ){
		var url_edit = "/forum/categories/edit/category="+ $(this).attr('category_id') + "/";
		var url_delete = "/forum/categories/remove/category="+ $(this).attr('category_id') + "/";
		var url_restore = "/forum/categories/restore/category="+ $(this).attr('category_id') + "/";
	}else{
		var url_edit = "#";
		var url_delete = "#";
		var url_restore = "#";
	};
	$("#button-category-edit").attr("href",url_edit);
	$("#button-category-delete").attr("href",url_delete);
	$("#button-category-restore").attr("href",url_restore);
});

//TOPIC
$("input[name='radio_topic']").change(function(){
	if($(this).prop( "checked", true ) ){
		var url_delete = "/forum/topics/remove/category="+ $(this).attr('category_id') + "/topic="+ $(this).attr('topic_id') +"/";
		var url_restore = "/forum/topics/restore/category="+ $(this).attr('category_id') + "/topic="+ $(this).attr('topic_id') +"/";
	}else{
		var url_delete = "#";
		var url_restore = "#";
	};
	$("#button-topic-delete").attr("href",url_delete);
	$("#button-topic-restore").attr("href",url_restore);
});

//PERSON
$("input[name='radio_person']").change(function(){
	if($(this).prop( "checked", true ) ){
		var url_delete = "/home/manager/persons/remove/person_type="+ $(this).attr('person_type') +"/person="+ $(this).attr('person_id') +"/";
		var url_restore = "/home/manager/persons/restore/person_type="+ $(this).attr('person_type') +"/person="+ $(this).attr('person_id') +"/";
	}else{
		var url_delete = "#";
		var url_restore = "#";
	};
	$("#button-person-delete").attr("href",url_delete);
	$("#button-person-restore").attr("href",url_restore);
});

//MESSAGE
$("input[name='radio_message']").change(function(){
	if($(this).prop( "checked", true ) ){
		var url_delete = "/home/manager/messages/remove/message="+ $(this).attr('message_id') +"/";
		var url_restore = "/home/manager/messages/restore/message="+ $(this).attr('message_id') +"/";
	}else{
		var url_delete = "#";
		var url_restore = "#";
	};
	$("#button-message-delete").attr("href",url_delete);
	$("#button-message-restore").attr("href",url_restore);
});

//Key
$("input[name='radio_register_key']").change(function(){
	if($(this).prop( "checked", true ) ){
		var url_delete = "/home/manager/persons/remove_registerkey/person_type="+ $(this).attr('person_type') +"/registerkey="+ $(this).attr('register_key_id') +"/";
	}else{
		var url_delete = "#";
	};
	$("#button-register_key-delete").attr("href",url_delete);
});