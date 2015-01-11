
$(document).ready(function(){
	$("#navOpcoes").click(function(){
		if($("#corpo").is(':hidden') ){
			$("#corpo").show('slow');
		}else{
			$("#corpo").hide('slow');
		};
	});
});