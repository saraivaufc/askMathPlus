/* Click */
$(document).ready(function(){
	$("#navOpcoes").click(function(){
		if($("#corpo").is(':hidden') ){
			$("#corpo").show('fast');
		}else{
			$("#corpo").hide('fast');
		};
	});
});









/* CSS */

$(document).ready(function(){
	var oldContainer
	$("#lista-perguntas").sortable({
		 group: 'nested',
		 afterMove: function (placeholder, container) {
		    	if(oldContainer != container){
		      		if(oldContainer)
		        			oldContainer.el.removeClass("active")
		      		container.el.addClass("active")
		      		oldContainer = container
		    	}
		  },
		  onDrop: function (item, container, _super) {
		    	container.el.removeClass("active");
		  	_super(item);
		  	atualizarLista();
		  }
	})

	$(".switch-container").on("click", ".switch", function  (e) {
	  	var method = $(this).hasClass("active") ? "enable" : "disable"
	 	$(e.delegateTarget).next().sortable(method)
	})
});

function atualizarLista(){
	var  perguntas= $("ul li").filter("[name='pergunta']");
	var conteudo = $("#conteudo_atual").val();
	var ids = new Object();
	var index = 0;
	$.each( perguntas , function(){
		ids[index++] = $(this).val();
	});

	data = new Object();
	data['conteudo'] = conteudo;
	data['perguntas'] = JSON.stringify(ids);
	data['csrfmiddlewaretoken'] = $("input[name='csrfmiddlewaretoken']").val();

	$.post("/ordena_perguntas/", data);


};