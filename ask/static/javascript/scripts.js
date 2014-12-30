




//CLICKS
$(document).ready(function(){


	$("#voltar-contato").click(function(){ 
		$.ajax({
			"url": "/is_logado/",
			"type": "get",
			"dataType": "html",
			"success": function(data) {
				if(data == "1"){
					window.location = '/principal/';
				}else{
					window.location = '/login/';
				}			
			},
			"error": function(jqXHR, status, error) {
				alert("status:" + status + "error:" + error);
			}
		});	
	});

	$("#responder").click(function(){
		var radios = $('input[name=opcao]', '#perguntas');
		for(var i=0; i< radios.length; i++){
			if(!radios[i].checked){
				radios[i].disabled = true;
			}
		}
		var res = verificarAcerto();
		var corContinuar;
		if(res){
			alert("Voce Acertou!!!");
		}else{
			alert("Voce Errou!!!");
		};

		$("#perguntas").submit();

	});

	$("#pular").click(function(){
		if(confirmPular() == false){
			return;
		}

		var url = "/atualiza_estado/" + $("#conteudo_atual").val() + "/" + $("#pergunta_atual").val() + "/";
		$.ajax({
			"url": url,
			"type": "get",
			"dataType": "html",
			async: false,
			"success": function(data){
				if(data == "None"){
					alert("Pergunta nao Possui item Correto, contactar o Administrador...");	
				}
				url = "/pulo/" + $("#conteudo_atual").val() + "/" + $("#pergunta_atual").val() + "/";
				$.ajax({
					"url": url,
					"type": "get",
					"dataType": "html",
					async: false,
					"success": function(){

					},
					"error": function(jqXHR, status, error) {
						alert(url);
						alert(error);
						
					}
				});
				window.location = window.location;
			},
			"error": function(jqXHR, status, error) {
				alert(error);
				alert(url);
			}
		});
	});

	$("input[name='opcao']").click(function(){
			$("#responder").removeAttr('disabled');
	});

	$("#ajuda").click(function(){
		var valor = $("#pergunta_atual").val();
		var url = "/ajuda/" + valor+"/";
		$.ajax({
			"url": url,
			"type": "get",
			"dataType": "html",
			async: false
		}).done(function(data){
			$("#ajuda_text").empty();
			$("#ajuda_text").append(data);
			var conteudo = $("#conteudo_atual").val();
			url = "/busca_ajuda/" + conteudo + "/";
			$.ajax({
				"url": url,
				"type": "get",
				"dataType": "html",
				async: true
			}).done(function(data){
				
			});		
		});


	});

});

//HOVERS

$(document).ready(function(){

});


//LEAVES
$(document).ready(function(){

});


//mudando o css

$(document).ready(function(){
	LatexIT.add('t',true);

	//$('.conteudo').jScrollPane({showArrows: true});
    $('#conteudo-left').jScrollPane({showArrows: true});
    $('.descricao-pergunta').jScrollPane({showArrows: true});

	$("#responder").attr('disabled', 'disabled');
	$("#li-botao").css({"margin-left": "5px" }); 	
});

function verificarAcerto(){
	var opcao = document.forms.perguntas.opcao.value;
	var pergunta = document.forms.perguntas.pergunta_atual.value;
	var conteudo = document.forms.perguntas.conteudo_atual.value;
	var myURL = "/" + conteudo + "/" + pergunta + "/" + opcao+"/";
	var res;
	$.ajax({
		"url": myURL,
		"type": "get",
		"dataType": "html",
		async: false
	}).done(function(data){
		if(data === "TRUE"){
			res = true;
		}else if(data === "FALSE"){
			res = false;
		}
	});
	return res;
};

function confirmPular(){
	return window.confirm("Deseja Pular a Pergunta?");
}


function sleep(millis){
	var date = new Date();
	var curDate = null;
  	do { 
  		curDate = new Date(); 
  	}while(curDate-date < millis);
}