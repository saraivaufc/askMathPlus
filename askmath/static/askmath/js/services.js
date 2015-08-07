var searchValues = [];
$(function(){
	$.get("/services/disciplines/get/", function(data){
		var disciplines = JSON.parse(data);
		for(var i=0 ; i< disciplines.length; i++){
			searchValues.push(disciplines[i].fields.title);
		}
	});
	$.get("/services/lessons/get/", function(data){
		var lessons = JSON.parse(data);
		for(var i=0 ; i< lessons.length; i++){
			searchValues.push(lessons[i].fields.title);
		}
	});
	$("#search").autocomplete({
		source: searchValues
	});
});