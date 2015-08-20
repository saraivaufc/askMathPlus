function pop(object, msn){
	object.popover({'placement':'top', 'content': msn});
	object.popover('show');
}

$(function(){
	/* DUMP */
	$('[data-popover="dump"]').mouseenter(function(){
		pop($(this),'If you want to view the deleted items, click here!');
	});
	
	/* UNDO */
	$('[data-popover="undo"]').mouseenter(function(){
		pop($(this), 'If you want to view the items active again, click here!');
	});
	
	
	
	$('[data-popover]').mouseleave(function(){
		$(this).popover('hide');
	});
	
	
});