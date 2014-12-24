




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

	$("#verificar").click(function(){
		var radios = $('input[name=opcao]', '#perguntas');
		for(var i=0; i< radios.length; i++){
			if(!radios[i].checked){
				radios[i].disabled = true;
			}
		}
		var res = verificarAcerto();
		var corContinuar;
		if(res){
			$(".barra-responder").addClass("bg-success");
			$(".conteudo-right").addClass("bg-success");
			$("#resultado_positivo").removeClass("hidden");
		}else{
			$(".barra-responder").addClass("bg-danger");
			$(".conteudo-right").addClass("bg-danger");
			$("#resultado_negativo").removeClass("hidden");
			
			var valor = $('input[name=opcao]:checked', '#perguntas').val();
			var url = "/ajuda/" + valor+"/";
			$.ajax({
				"url": url,
				"type": "get",
				"dataType": "html",
				async: false
			}).done(function(data){
				if (data != "None"){
					$("#ajuda").css("visibility","visible");
				}		
			});
				
		};

		$(this).text("Continuar");
			$(this).attr('id',"continuar");
			$("#continuar").click(function(){
				$("#perguntas").submit();
		});
		$("#pular").attr('disabled', 'disabled');
		$("#voltar").hide();

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
			"success": function(){
				url = "/pulo/" + $("#conteudo_atual").val() + "/" + $("#pergunta_atual").val() + "/";
				$.ajax({
					"url": url,
					"type": "get",
					"dataType": "html",
					async: false,
					"success": function(){

					},
					"error": function(jqXHR, status, error) {
						alert(error);
						alert(url);
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
			$("#verificar").removeAttr('disabled');
	});

	$("#ajuda").click(function(){
		var valor = $('input[name=opcao]:checked', '#perguntas').val();
		var url = "/ajuda/" + valor+"/";
		$.ajax({
			"url": url,
			"type": "get",
			"dataType": "html",
			async: false
		}).done(function(data){
			$("#ajuda_text").empty();
			$("#ajuda_text").append(data);
			var pergunta = $("#pergunta_atual").val();
			url = "/busca_ajuda/" + pergunta + "/"  + valor+"/";
			$.ajax({
					"url": url,
					"type": "get",
					"dataType": "html",
					async: false
				}).done(function(data){});
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
    $('#conteudo-left').jScrollPane();
    $('.descricao-pergunta').jScrollPane();

	$("#verificar").attr('disabled', 'disabled');
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