from askmath.views.manager import ProxyLesson
from django.conf.urls import patterns, url

proxy_category = ProxyLesson()

urlpatterns = patterns('',
	url(r'^view/lesson=(?P<id_lesson>\d+)/$', proxy_category.view_lesson, name="manager_lesson_view"),
	url(r'^add/discipline=(?P<id_discipline>\d+)/$', proxy_category.add_lesson, name="manager_lesson_add"),
	url(r'^remove/lesson=(?P<id_lesson>\d+)/$', proxy_category.remove_lesson, name="manager_lesson_remove"),
	url(r'^edit/lesson=(?P<id_lesson>\d+)/$', proxy_category.edit_lesson, name="manager_lesson_edit"),
	url(r'^restore/lesson=(?P<id_lesson>\d+)/$', proxy_category.restore_lesson, name="manager_lesson_restore"),
)
