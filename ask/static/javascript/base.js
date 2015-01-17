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
	$("ul.list-group").sortable({
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
		  	alert("cas");
		  }
	})

	$(".switch-container").on("click", ".switch", function  (e) {
	  	var method = $(this).hasClass("active") ? "enable" : "disable"
	 	$(e.delegateTarget).next().sortable(method)
	})
});