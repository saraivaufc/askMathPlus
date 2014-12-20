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


$(document).ready(function() {
    //$('.conteudo').jScrollPane({showArrows: true});
    $('.metro').jScrollPane({showArrows: true});
    $('.conteudo-left').jScrollPane({showArrows: true});
    $('.descricao-pergunta').jScrollPane({showArrows: true});
});

$(document).ready(function (){
		var cores = "turquoise.emerald.peter-river.amethyst.wet-asphalt.green-sea.nephritis.belize-hole.wisteria.midnight-blue.sun-flower.carrot.alizarin.concrete.orange.pumpkin.pomegranate.asbestos";
		var coresLista = cores.split(".");
		coresLista.reverse();
		var selecionadas = [];
		$(".tile").each(function(){
			var cor = coresLista.pop();
			console.log(cor);
			$(this).addClass(cor);
			selecionadas.push(cor);
			if(coresLista.length == 0){
				for(var i=0; i< selecionadas.length; i++){
					coresLista.push(selecionadas[i]);
				}
				selecionadas = [];
			}
		});
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
	window.location.href= "/principal/"+ text2+"/";
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



$(document).ready(function(){
	LatexIT.add('t',true);

	$("#verificar").attr('disabled', 'disabled');	

	$("#verificar").click(function(){
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

		$(".descricao-pergunta").fadeTo('slow',.6);
		$(".descricao-pergunta").append('<div style="position: absolute;top:0;left:0;width: 100%;height:100%;z-index:2;opacity:0.4;filter: alpha(opacity = 50)"></div>');



	});

	$("#pular").click(function(){
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