function pop(object, msn, placement){
	placement = placement || "top";
	object.popover({'placement': placement, 'content': msn});
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
	
	/* SORT */
	$('[data-popover="sort"]').mouseenter(function(){
		pop($(this), 'You can order these items, click here!');
	});
	
	
	
	$('[data-popover]').mouseleave(function(){
		$(this).popover('hide');
	});
	
	
});