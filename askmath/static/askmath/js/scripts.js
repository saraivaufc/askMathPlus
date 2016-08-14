function Init() {
	Preview.Init();
};


(function ($) {
	$(document).ready(function ($) {
		$('#feedback-modal').on('shown.bs.modal', function () {
			document.getElementById('feedback-url').value = window.location.protocol + '//' + window.location.hostname + window.location.pathname + window.location.hash;

			$('#feedback-alerts').empty();
			var $form = $('#feedback-form');
			$form.removeClass('loading');
			$('input:visible:first', $form).focus();
		});

		$('#feedback-form').on('submit', function (e) {
			var $form = $('#feedback-form');
			var $modal = $('#feedback-modal');
			var $alerts = $('#feedback-alerts');

			$form.addClass('loading');
			$alerts.empty();
			$.post(
				$form.attr('action'),
				$form.serialize(),
				function (response) {
					if (response.ok) {
						$alerts.append('<p class="alert alert-success">' + response.message + '</p>');

						setTimeout(function () {
							$modal.modal('hide');
							$alerts.empty();
							$form.trigger('reset');
						}, 1000);

					} else {
						$alerts.append('<p class="alert alert-danger">' + response.message + '</p>');
					}
					$form.removeClass('loading');
				}, 'json'
			);

			e.preventDefault(); // not submit form
		});
	});
})(jQuery);

function resize_window() {
	var site = parseInt($("#site").css("height"));
	var footer = parseInt($("#footer").css("height"));
	$("#site").css("min-height", (site - footer) + "px");
}

$(function(){
	resize_window();
	$(window).resize(resize_window);
})

$(function () {
	$('.button-checkbox').each(function () {

		// Settings
		var $widget = $(this),
			$button = $widget.find('button'),
			$checkbox = $widget.find('input:checkbox'),
			color = $button.data('color'),
			settings = {
				on: {
					icon: 'glyphicon glyphicon-check'
				},
				off: {
					icon: 'glyphicon glyphicon-unchecked'
				}
			};

		// Event Handlers
		$button.on('click', function () {
			$checkbox.prop('checked', !$checkbox.is(':checked'));
			$checkbox.triggerHandler('change');
			updateDisplay();
		});
		$checkbox.on('change', function () {
			updateDisplay();
		});

		// Actions
		function updateDisplay() {
			var isChecked = $checkbox.is(':checked');

			// Set the button's state
			$button.data('state', (isChecked) ? "on" : "off");

			// Set the button's icon
			$button.find('.state-icon')
				.removeClass()
				.addClass('state-icon ' + settings[$button.data('state')].icon);

			// Update the button's color
			if (isChecked) {
				$button
					.removeClass('btn-default')
					.addClass('btn-' + color + ' active');
			}
			else {
				$button
					.removeClass('btn-' + color + ' active')
					.addClass('btn-default');
			}
		}

		// Initialization
		function init() {

			updateDisplay();

			// Inject the icon if applicable
			if ($button.find('.state-icon').length == 0) {
				$button.prepend('<i class="state-icon ' + settings[$button.data('state')].icon + '"></i>');
			}
		}

		init();
	});
});

$("[type=file]").on("change", function () {
	// Name of file and placeholder
	var file = this.files[0].name;
	var dflt = $(this).attr("placeholder");
	if ($(this).val() != "") {
		$(this).next().text(file);
	} else {
		$(this).next().text(dflt);
	}
});


$(function () {
	$("#list_questions_sort").sortable();
	$("#list_videos_sort").sortable();
});

function sleep(ms) {
	var unixtime_ms = new Date().getTime();
	while (new Date().getTime() < unixtime_ms + ms) {
	}
}

function sortQuestions() {
	var list = $("#list_questions_sort");
	var order = [];
	list.find(".list").each(function () {
		try {
			order.push(parseInt($(this).attr("value")));
		} catch (e) {
			alert("Error sort questions!!!");
		}
	});
	var url = window.location.href;
	data = new Object();
	data['new_order'] = JSON.stringify(order);
	data['csrfmiddlewaretoken'] = $("input[name='csrfmiddlewaretoken']").val();
	$.post(url, data, function (data) {
		$.Notify({
			caption: 'Success',
			content: "Questions Sorted Success!!!",
			type: 'success',
		});
	});
};

function sortVideos() {
	var list = $("#list_videos_sort");
	var order = [];
	list.find(".list").each(function () {
		try {
			order.push(parseInt($(this).attr("value")));
		} catch (e) {
			$.Notify({
				caption: 'Error',
				content: "Erro sort videos!!!",
				type: 'danger',
			});
		}
	});
	var url = window.location.href;
	data = new Object();
	data['new_order'] = JSON.stringify(order);
	data['csrfmiddlewaretoken'] = $("input[name='csrfmiddlewaretoken']").val();
	$.post(url, data, function (data) {
		$.Notify({
			caption: 'Success',
			content: "Videos Sorted Success!!!",
			type: 'success',
		});
	});
};

function help() {
	var url_help = $("input[name='url_help']").val();
	try {
		$.get(url_help, function (data) {});
	} catch (e) {
		console.log(e);
	}
};

$(function () {
	$(".latex").each(function () {
		$(this).keyup(function () {
			Preview.Update();
		});
	});
});


$("#btn-help").on('click', help);


function openEditor(box) {
	var id = box.attr("id");
	$('#box-latex').attr('value', id);
	$("#latex_formula").val(box.val());
	Preview.Update();
	$('#box-latex').modal();
}

$(function () {

	$("#latex_formula").on('keyup', function () {
		var latex = $(this).val();
		var result = document.getElementById("MathPreview");
		typejax.updater.init(latex, latex.length, result);
	});

	$("#box-latex-submit").click(function () {
		var text = $("#latex_formula").val();
		$("#latex_formula").val("");
		var input_form = $("#" + $('#box-latex').attr('value'));
		input_form.val(text);
		$('#box-latex').modal('hide');
	});
	
});

function showKey() {
	$("input[name='key']").removeAttr("disabled");
	$("label[for='id_key']").css({'display': 'block'});
	$("input[name='key']").css({'display': 'block'});
	$("input[name='key']").attr("required", "required");
}

function hideKey() {
	$("input[name='key']").removeAttr("required");
	$("input[name='key']").attr("disabled", "disabled");
	$("label[for='id_key']").css({'display': 'none'});
	$("input[name='key']").css({'display': 'none'});
}

$(function () {
	hideKey();
	$("select[name='group']").change(function () {
		if ($(this).val() != "student") {
			showKey();
		} else {
			hideKey();
		}
	});

});

$(function () {
	$("#back").click(function () {
		window.history.back();
	});
});

$(function () {
	$(".button-like").click(function () {
		var $button = $(this);
		var href = $(this).attr("href");
		if ($(this).hasClass("bg-green")) {
			$.get(href).done(function (data) {
				try {
					var data = JSON.parse(data);
					if (data['result'] == "True") {
						unlike($button, data['value']);
					}
				} catch (e) {
					console.log(e);
				}
			});
		} else {
			$.get(href).done(function (data) {
				try {
					var data = JSON.parse(data);
					if (data['result'] == "True") {
						like($button, data['value']);
					}
				} catch (e) {
					console.log(e);
				}
			});
		}
		;
	});
});


function like(buttom, likes) {
	var like_count = buttom.find(".like-count");
	try {
		likes = parseInt(likes);
	} catch (e) {
		likes = parsetInt(like_count.html()) + 1;
	}
	buttom.removeClass("bg-gray");
	buttom.addClass("bg-green");
	buttom.find(".icon").addClass("bg-emerald");
	like_count.text(likes);
	var href = buttom.attr("href");
	buttom.attr("href", href.replace("/like", "/unlike"));
}

function unlike(buttom, likes) {
	var like_count = buttom.find(".like-count");
	try {
		likes = parseInt(likes);
	} catch (e) {
		likes = parsetInt(like_count.html()) - 1;
	}
	buttom.addClass("bg-gray");
	buttom.removeClass("bg-green");
	buttom.find(".icon").removeClass("bg-emerald");
	like_count.text(likes);
	var href = buttom.attr("href");
	buttom.attr("href", href.replace("/unlike", "/like"));
}


$(function () {
	$(".latex").each(function () {
		var id = $(this).attr("id");
		$(this).parent().prepend("<span value='" + id + "'  class='button-latex right mif-file-code'></span>");
	});
	$(".button-latex").click(function () {
		var id = $(this).attr('value');
		var box = $('#' + id);
		openEditor(box);
	});

});

$(function () {
	$(".comment-edit").on('click', function () {
		var url = $(this).attr("url");
		var id = $(this).attr("href");
		$(id).attr("temp", $(id).text())
		$(id).html('<form class="form" action="' + url + '" method="post"><div class="input-control textarea full-size no-padding"><textarea id="id_description" name="description" required col="100%">' + $(id).text() + '</textarea></div><button class="button button-default cancel">Cancel</button><button type="submit" class="button button-primary">Edit</button></form>');
		$(id).find(".form").submit(function () {
			var csrftoken = Cookies.get('csrftoken');
			data = new Object();
			data['description'] = $(this).find("#id_description").val();
			data['csrfmiddlewaretoken'] = csrftoken;
			$.post(url, data, function (data) {
				try {
					var data = JSON.parse(data);
					if (data['result'] == 'True') {
						var textarea = $(id).find(".form").find("#id_description");
						var text = textarea.val();
						textarea.remove();
						$(id).text(text);
					} else {
					}
				} catch (e) {
				}
			});
			return false;
		});

		$(id).find(".form").find(".cancel").click(function () {
			var textarea = $(id).find(".form").find("#id_description");
			var text = $(id).attr("temp");
			textarea.remove();
			$(id).text(text);
		});
	})
});

$(function () {
	$(".accordion").accordion();
});

$(function () {
	$("#id_color").each(function () {
		$(this).find("option").each(function () {
			$(this).addClass($(this).val());
		});
	});
})

function showCharm(id) {
	var charm = $(id).data("charm");
	if (charm.element.data("opened") === true) {
		charm.close();
	} else {
		charm.open();
	}
}

function showDialog(id) {
	 var dialog = $(id).data('dialog');
	if (!dialog.element.data('opened')) {
		dialog.open();
	} else {
		dialog.close();
	}
}

var isMobile = {
	Android: function () {
		return navigator.userAgent.match(/Android/i);
	},
	BlackBerry: function () {
		return navigator.userAgent.match(/BlackBerry/i);
	},
	iOS: function () {
		return navigator.userAgent.match(/iPhone|iPad|iPod/i);
	},
	Opera: function () {
		return navigator.userAgent.match(/Opera Mini/i);
	},
	Windows: function () {
		return navigator.userAgent.match(/IEMobile/i) || navigator.userAgent.match(/WPDesktop/i);
	},
	any: function () {
		return (isMobile.Android() || isMobile.BlackBerry() || isMobile.iOS() || isMobile.Opera() || isMobile.Windows());
	}
};

$(function () {
	$("#signUpForm  input[name=confirm_password]").change(function () {

		if ($("#signUpForm input[name='password']").text() != $("#signUpForm input[name='confirm_password']").text()) {
			$("#signUpForm input[name='password']").css("border", "#FF0000 solid 1px")
			$("#signUpForm input[name='confirm_password']").css("border", "#FF0000 solid 1px")
		} else {
			$("#signUpForm input[name='password']").css("border", "#FFF solid 0px");
			$("#signUpForm input[name='confirm_password']").css("border", "#FFF solid 0px");
		}
	});
});


$(function () {
	$('#select_classe_default').on('change', function(){
		if($(this).val()) {
			window.location = $(this).val();
		}
	})
})
