$(function(){
	if(readCookie("contrast")){
		$("body").addClass("bg-dark fg-white");	
		$("a, h1, h2, h3").addClass("link_contrast");
		$(".btn").addClass("btn_contrast");
		var button_contrast = $("#button-contrast");
		button_contrast.removeClass("disable-contrast");
		button_contrast.addClass("enable-contrast");
		button_contrast.text("High Contrast-ON [3]");
	}
	if(readCookie("font")){
		font_plus();
		var button_font = $("#button-font");
		button_font.removeClass("font-minus");
		button_font.addClass("font-plus");
		button_font.text("Big Font-ON [4]");
	}
});

$("#button-contrast").click(function(){
	$("body").toggleClass("bg-dark fg-white");
	$("a, h1, h2, h3").toggleClass("link_contrast");
	$(".btn").toggleClass("btn_contrast");
	if($(this).hasClass("disable-contrast")){
		$(this).removeClass("disable-contrast");
		$(this).addClass("enable-contrast");
		$(this).text("High Contrast-ON [3]");
		generateCookie("contrast", true , 7);
		console.log("Contrar Enable");
	}else if($(this).hasClass("enable-contrast")){
		$(this).removeClass("enable-contrast");
		$(this).addClass("disable-contrast");
		$(this).text("High Contrast-OFF [3]");
		eraseCookie("contrast");
		console.log("Contrar Disable");
	}
});

$("#increase-font").click(function(){
	font_plus();
});

$("#decrease-font").click(function(){
	font_minus();
});


function font_plus(){
	$("*e").each(function(){
		var font = parseInt($(this).css("font-size")) + 1;
		$(this).css({"font-size": font + "px" });
	});
}

function font_minus(){
	var font_p = $("p").css("font-size") - 4;
	var font_a = $("a").css("font-size") - 4;
	$("p").css({"font-size": font_p + "px" });
	$("a").css({"font-size": font_a + "px" });
}