from askmath.views.content import ProxyQuestion
from django.conf.urls import patterns, url

proxy_category = ProxyQuestion()

urlpatterns = patterns('',
	 url(r'^view_question/discipline=(?P<id_discipline>\d+)/lesson=(?P<id_lesson>\d+)/$',
		proxy_category.view_question, name="content_question_view"),
	 url(r'^view_question/discipline=(?P<id_discipline>\d+)/lesson=(?P<id_lesson>\d+)/question=(?P<id_question>\d+)/$',
		proxy_category.view_question, name="content_question_view"),
	 url(r'^answer_question/discipline=(?P<id_discipline>\d+)/lesson=(?P<id_lesson>\d+)/question=(?P<id_question>\d+)/$',
		proxy_category.answer_question, name="content_question_answer"),
	 url(r'^jump_question/discipline=(?P<id_discipline>\d+)/lesson=(?P<id_lesson>\d+)/question=(?P<id_question>\d+)/$',
		proxy_category.jump_question, name="content_question_jump"),
	 url(r'^choose_skipped_question/discipline=(?P<id_discipline>\d+)/lesson=(?P<id_lesson>\d+)/question=(?P<id_question>\d+)/$',
		proxy_category.choose_skipped_question, name="content_question_choose_skipped"),
	 url(r'^help/discipline=(?P<id_discipline>\d+)/lesson=(?P<id_lesson>\d+)/question=(?P<id_question>\d+)/$',
		proxy_category.help_question, name="content_question_help"),
	 url(r'^reset_lesson/discipline=(?P<id_discipline>\d+)/lesson=(?P<id_lesson>\d+)/$',
	 	proxy_category.reset_lesson, name="content_question_reset_lesson"),
	 url(r'^view_history/discipline=(?P<id_discipline>\d+)/lesson=(?P<id_lesson>\d+)/$',
	 	proxy_category.view_history, name="content_question_history"),
)
