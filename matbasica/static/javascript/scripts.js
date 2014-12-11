
function sleep(millis)
 {
  var date = new Date();
  var curDate = null;
  do { 
  	curDate = new Date(); 
  }while(curDate-date < millis);
}


$(function () {
	var maiorLinha = 0;
	$(".metro .linha").each(function () {
		var larguraLinha = 0;
		$(this).children(".tile").each(function () {
			larguraLinha += $(this).width();
			larguraLinha += 2*parseInt($(this).css("margin-right").toString().replace("px", ""));
		});
		if (larguraLinha > maiorLinha)
			maiorLinha = larguraLinha+5;
		});
		$(".container").css("width", maiorLinha.toString() + "px");
});

$(".tile").each(function (){
		var ran =  Math.floor((Math.random() * 8) + 1);
		switch(ran) {
		case 1:
			$(this).addClass("teal-light");
			break;
		case 2:
			$(this).addClass("blue-light");
			break;
		case 3:
			$(this).addClass("purple-light");
			break;
		case 4:
			$(this).addClass("dark-purple-light");
			break;
		case 5:
			$(this).addClass("red-light");
			break;
		case 6:
			$(this).addClass("green-light");
			break;
		case 7:
			$(this).addClass("orange-light");
			break;
		case 8:
			$(this).addClass("sky-blue-light");
			break;
		default:
			$(this).addClass("red");
		}
		sleep(10);
});

$(".tile").each(function () {
			$(this).css("width", $(this).height());
});
$(".tileLargo").each(function () {
			$(this).css("width", ($(this).height() * 2) + 10);
});


$("#li-botao").css({"margin-left": "5px" }); 

$(".tile").click(function() {
	var text =  $(this).children(".font-metro").children("#text-quadrado").children("#cont").text();
	var text2 = text.split(" ").join("_");
	window.location.href= "/principal/".concat(text2);
	$(this).addClass("selecionado");
});

$(".tile").hover(function(){
	$(this).addClass("selecionado");
});

$(".tile").mouseleave(function () {
	$(this).removeClass("selecionado");
});

function verificarAcerto(){
	var opcao = document.forms.perguntas.opcao.value;
	var pergunta = document.forms.perguntas.pergunta_atual.value;
	var conteudo = document.forms.perguntas.conteudo_atual.value;
	var myURL = "/" + conteudo + "/" + pergunta + "/" + opcao;
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

$("#voltar-contato").click(function(){ 
	$.ajax({
		"url": "/is_logado",
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



$(document).ready(function(){
	LatexIT.add('t',true);

	$("#verificar").attr('disabled', 'disabled');
	$("#ajuda").hide();	

	$("#verificar").click(function(){
		var res = verificarAcerto();
		if(res){
			$("#barra-responder").css("background-color","#DEF0A5");
			$("#resultado_positivo").removeClass("hidden");
		}else{
			$("#barra-responder").css("background-color", "#FFD4CC");
			$("#resultado_negativo").removeClass("hidden");
			$("#ajuda").show(1000);
		};

		$(this).text("Continuar");
			$(this).attr('id',"continuar");
			$("#continuar").click(function(){
				$("#perguntas").submit();
		});
		$("#pular").attr('disabled', 'disabled');

		var form =  document.forms.perguntas;
		nElements = form.length;
		for (i=0; i<nElements; i++){
			if (form[i].type == "radio"){
				//form[i].disabled = true;
			}
		} 
		$("#form-perguntas").fadeTo('slow',.6);
		$("#form-perguntas").append('<div style="position: absolute;top:0;left:0;width: 100%;height:100%;z-index:2;opacity:0.4;filter: alpha(opacity = 50)"></div>');

	});

	$("#pular").click(function(){
		var url = "/atualiza_estado/" + $("#conteudo_atual").val() + "/" + $("#pergunta_atual").val() + "/";
		$.ajax({
			"url": url,
			"type": "get",
			"dataType": "html",
			"success": function(){
				window.location.href=window.location.href;
			},
			"error": function(jqXHR, status, error) {
				//adicionar algo aqui
			}
		});
	});

	$("input[name='opcao']").click(function(){
			$("#verificar").removeAttr('disabled');
	});

	$("#ajuda").click(function(){
		var valor = $('input[name=opcao]:checked', '#perguntas').val();
		var url = "/ajuda/" + valor;
		$.ajax({
			"url": url,
			"type": "get",
			"dataType": "html",
			async: false
		}).done(function(data){
			$("#ajuda_text").empty(); 
			$("#ajuda_text").append(data);
		});
	});
});