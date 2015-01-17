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
	var adjustment

	$("ul.lista_perguntas").sortable({
		 group: 'simple_with_animation',
		 pullPlaceholder: false,
		  
		  onDrop: function  (item, targetContainer, _super) {
		 	var clonedItem = $('<li/>').css({height: 0})
		    	item.before(clonedItem)
		    	clonedItem.animate({'height': item.height()});
		    
		    	item.animate(clonedItem.position(), function  () {
			      	clonedItem.detach();
			      	_super(item);
		    	});
		    	atualizarLista();
		},

		  // set item relative to cursor position
		onDragStart: function ($item, container, _super) {
		 	var offset = $item.offset(),
		    	pointer = container.rootGroup.pointer

		    	adjustment = {
		      		left: pointer.left - offset.left,
		      		top: pointer.top - offset.top
		    	}

		    	_super($item, container);
		},
		onDrag: function ($item, position) {
		 	$item.css({
		      		left: position.left - adjustment.left,
		      		top: position.top - adjustment.top
		    	})
		 }
	})
});

function atualizarLista(){
	var  perguntas= $("ul.perguntas_ordenadas li").filter("[name='pergunta']");
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