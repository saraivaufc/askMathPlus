
//CLICKS
$(document).ready(function(){

	$("#ajuda").click(function(){
		var valor = $("#pergunta_atual").val();
		var url = "/ajuda/" + valor+"/";
		$.ajax({
			"url": url,
			"type": "get",
			"dataType": "html",
			async: false
		}).done(function(data){
			$("#ajuda_text").empty().append(data);
		});
	});

	$(".glyphicon-plus").click(function(){
		var opcao = $(this).parent().attr("value");
		 window.location = "/gerenciador/add/" + opcao + "/";
	});

	$(".glyphicon-remove").click(function(){
		var opcao = $(this).parent().attr("value");
		 window.location = "/gerenciador/rem/" + opcao + "/";
	});

	$(".glyphicon-edit").click(function(){
		var opcao = $(this).parent().attr("value");
		 window.location = "/gerenciador/edit/" + opcao + "/";
	});


});

//HOVERS

$(document).ready(function(){
	$("#gerenciador").hover(function(){
		$("#gerenciador").popover('show');
	});
	$("#editor-latex").hover(function(){
		$("#editor-latex").popover('show');
	});
	$("#forum").hover(function(){
		$("#forum").popover('show');
	});
});


//LEAVES
$(document).ready(function(){
	$("#gerenciador").mouseleave(function(){
		$("#gerenciador").popover('hide');
	});
	$("#editor-latex").mouseleave(function(){
		$("#editor-latex").popover('hide');
	});
	$("#forum").mouseleave(function(){
		$("#forum").popover('hide');
	});
});


//mudando o css

$(document).ready(function(){
	LatexIT.add('t',true);
	//$('.conteudo').jScrollPane({showArrows: true});
    $('#conteudo-left').jScrollPane({showArrows: true});
    $('.descricao-pergunta').jScrollPane({showArrows: true}); 	
});
