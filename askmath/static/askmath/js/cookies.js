
/**
 * strCookie = Nome do cookie
 * strValor = Valor que será salvo no cookie
 * lngDias = Dias de validade do cookie
 */
function generateCookie(strCookie, strValue, lngDays) {
  	$.cookie(strCookie, strValue, {
    	expires : lngDays 
	});
	console.log("generateCookie");
}

/**
 * nomeCookie = Nome que foi dado ao cookie durante a criação
 */

function readCookie(nameCookie) {
	console.log("readCookie");
	return $.cookie(nameCookie);
}

/**
 * strCookie = Nome do cookie
 */
function eraseCookie(strCookie) {
	$.removeCookie(strCookie);
	console.log("removeCookie");
}