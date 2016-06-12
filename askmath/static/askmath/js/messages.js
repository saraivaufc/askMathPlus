
$("ul.messages > li.message").each(function(){
	var type = ""
	var caption = ""
	if( $(this).attr("value") == "success"){
		caption = "Sucesso";
		type = "success";
	}
	if( $(this).attr("value") == "error"){
		caption = "Erro";
		type = "alert";
	}

	$.Notify({
	    caption: caption,
	    content: $(this).text(),
	    type:  type,
	});
});