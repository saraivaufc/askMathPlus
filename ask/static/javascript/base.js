
$(document).ready(function(){
	$("#navOpcoes").click(function(){
		if($("#corpo").is(':hidden') ){
			$("#corpo").show('fast');
		}else{
			$("#corpo").hide('fast');
		};
	});
});