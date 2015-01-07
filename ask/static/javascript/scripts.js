




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
			bootbox.dialog({
			closeButton: false,
			message: '<h2 class="text-center" >Sua resposta esta correta!!!</h2>',
			buttons: {
				success: {
					label: "Continuar",
					className: "btn-success",
					callback: function() {
						$("#perguntas").submit();
					}
				}
			}
			}).find('.modal-content').css({'color': 'green', 'font-weight':'bold'});
		}else{
			bootbox.dialog({
			closeButton: false,
			message: '<h2 class="text-center" >Sua resposta esta incorreta!!!</h2>',
			buttons: {
				success: {
					label: "Continuar",
					className: "btn-success",
					callback: function() {
						$("#perguntas").submit();
					}
				}
			}
			}).find('.modal-content').css({'color': 'red', 'font-weight':'bold'});   
		};
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
			$("#ajuda_text").empty().append(data);
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

	$("input[name='opcao']").click(function(){
			$("#responder").removeAttr('disabled');
	});
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


function sleep(millis){
	var date = new Date();
	var curDate = null;
  	do { 
  		curDate = new Date(); 
  	}while(curDate-date < millis);
}

function pularPergunta(){
	var url = "/atualiza_estado/" + $("#conteudo_atual").val() + "/" + $("#pergunta_atual").val() + "/";
	$.ajax({
		"url": url,
		"type": "get",
		"dataType": "html",
		async: false,
		"success": function(data){
			if(data == "None"){
				bootbox.alert("Pergunta nao Possui item Correto, contactar o Administrador...");	
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
};