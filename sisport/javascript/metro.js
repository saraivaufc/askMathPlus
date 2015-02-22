
//aplicando o painel Metro
function createMetro(){
	$(document).ready(function() {
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
};

//mudando tamanho dos azulejos
function setSizeMetro(){
	$(document).ready(function(){
		$(".tile").each(function () {
					$(this).css("width", ($(this).height()) + "px" );
		});

		$(".tileLargo").each(function () {
					$(this).css("width", (($(this).height() * 2) + 10) + "px");
		});
	});
}



//mudando a cor do painel Metro
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

//CLICKS

$(document).ready(function(){
	$(".tile").click(function() {
		var text =  $(this).children(".font-metro").text();
		var text2 = text.split(" ").join("_");
		window.location.href= "/principal/opcoes/"+ text2+"/";
		$(this).addClass("selecionado");
	});
});


//HOVERS

$(document).ready(function(){
	$(".tile").hover(function(){
		$(this).addClass("selecionado");
	});

});

//LEAVES
$(document).ready(function(){
	$(".tile").mouseleave(function () {
		$(this).removeClass("selecionado");
	});
});


//mudando o css

$(document).ready(function(){
	//$('.conteudo').jScrollPane({showArrows: true});
    $('.metro').jScrollPane({showArrows: true}); 	
});
