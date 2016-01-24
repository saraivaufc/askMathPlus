$(function(){
	if(Cookies.get("contrast")){
		$("body").addClass("bg-dark fg-white");	
		$("a, h1, h2, h3").addClass("link_contrast");
		$(".btn").addClass("btn_contrast");
		var button_contrast = $("#button-contrast");
		button_contrast.removeClass("disable-contrast");
		button_contrast.addClass("enable-contrast");
		button_contrast.text("High Contrast-ON [3]");
	}
	var font_size  = Cookies.get("font");
	if(font_size === undefined){

	}else{
		set_font(font_size);
		var button_font = $("#button-font");
		button_font.removeClass("font-minus");
		button_font.addClass("font-plus");
		button_font.text("Big Font-ON [4]");
	
	}
});

$("#button-contrast").click(function(){
	$("body").toggleClass("highcontrast");
	if($(this).hasClass("disable-contrast")){
		$(this).removeClass("disable-contrast");
		$(this).addClass("enable-contrast");
		$(this).text("High Contrast-ON [3]");
		Cookies.set("contrast", true);
		console.log("Contrar Enable");
	}else if($(this).hasClass("enable-contrast")){
		$(this).removeClass("enable-contrast");
		$(this).addClass("disable-contrast");
		$(this).text("High Contrast-OFF [3]");
		Cookies.remove("contrast");
		console.log("Contrar Disable");
	}
});

$("#increase-font").click(function(){
	alter_font(2);
});

$("#decrease-font").click(function(){
	alter_font(-2);
});


function set_font(size){
	$("h1, h2, h3, h4, h5, h6, p, label, a").each(function(){
		var font = parseInt($(this).css("font-size")) + parseInt(size);
		$(this).css({"font-size": font + "px" });
	});
}

function alter_font(size){
	set_font(size);
	var font = Cookies.get("font");
	if(font === undefined){
		font = size;
	}else{
		font = parseInt(font) + parseInt(size);
	}
	Cookies.set("font", font);
}
