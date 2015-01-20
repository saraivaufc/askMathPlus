
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


function editTurma(id){
	window.location = "/gerenciador/edit/1/" +id + "/";
}


function remTurma(id){
	if(window.confirm("Deseja realmente remover essa Turma?")){
		$.get("/gerenciador/rem/1/" +id + "/", function(data){
			if(data == "True"){
				alert("Turma Removida com Sucesso!!!");
			}else{
				alert("Falha ao Remover Turma!!!");
			}
			window.location = window.location;
		});
	}
}

function editLicao(id){
	window.location = "/gerenciador/edit/2/" + id + "/";
}

function remLicao(id){
	if(window.confirm("Deseja realmente remover essa Licao?")){
		$.get("/gerenciador/rem/2/" +id + "/", function(data){
			if(data == "True"){
				alert("Licao Removida com Sucesso!!!");
			}else{
				alert("Falha ao Remover Licao!!!");
			}
			window.location = window.location;
		});
	}
}

function remPergunta(id){
	if(window.confirm("Deseja realmente remover essa Pergunta?")){
		$.get("/gerenciador/rem/3/" +id + "/", function(data){
			if(data == "True"){
				alert("Pergunta Removida com Sucesso!!!");
			}else{
				alert("Falha ao Remover Pergunta!!!");
			}
			window.location = window.location;
		});
	}
}