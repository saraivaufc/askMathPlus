var search_values = [];
$(function(){

	$(function(){
		$.get("/api/disciplines/?format=json", function(data){
			var topics = data;
			for(var i=0 ; i< topics.length; i++){
				search_values.push(topics[i].title);
			}
		});
		$.get("/api/lessons/?format=json", function(data){
			var items = data;
			for(var i=0 ; i< items.length; i++){
				search_values.push(items[i].title);
			}
		});
	});

	$("#search").autocomplete({
		source: search_values,
		open: function(){
	       	setTimeout(function () {
		           $('.ui-autocomplete').css('z-index', 99999999999999);
		      }, 0);
	    }
	});
});