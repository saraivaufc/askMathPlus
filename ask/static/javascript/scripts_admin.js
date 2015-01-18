
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

	$(".glyphicon-list-alt").click(function(){
		var opcao = $(this).parent().attr("value");
		 window.location = "/gerenciador/list/" + opcao + "/";
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


function remTurma(id){
	if(window.confirm("Deseja realmente remover essa Turma?")){
		window.location = "/gerenciador/rem/1/" +id + "/";
	}
}

function remLicao(id){
	if(window.confirm("Deseja realmente remover essa Licao?")){
		window.location = "/gerenciador/rem/2/" +id + "/";
	}
}

function remPergunta(id){
	if(window.confirm("Deseja realmente remover essa Pergunta?")){
			window.location = "/gerenciador/rem/3/" +id + "/";
	}
}

function remAjuda(id){
	if(window.confirm("Deseja realmente remover essa Ajuda?")){
		window.location = "/gerenciador/rem/4/" +id + "/";
	}
}

function remItem(id){
	if(window.confirm("Deseja realmente remover esse Item?")){
		window.location = "/gerenciador/rem/5/" +id + "/";
	}
}

function remDeficiencia(id){
	if(window.confirm("Deseja realmente remover essa Deficiencia?")){
		window.location = "/gerenciador/rem/6/" +id + "/";
	}
}