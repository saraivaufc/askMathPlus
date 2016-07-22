from askmath.views.manager import ProxyLesson
from django.conf.urls import patterns, url


proxy_category = ProxyLesson()  

urlpatterns = patterns('',
    url(r'^view/discipline=(?P<id_discipline>\d+)/$', proxy_category.view_lessons, name="manager_lesson_view"),
    url(r'^view_removed/discipline=(?P<id_discipline>\d+)/$', proxy_category.view_lessons_removed, name="manager_lesson_view_removed"),
    url(r'^add/discipline=(?P<id_discipline>\d+)/$', proxy_category.add_lesson, name="manager_lesson_add"),
    url(r'^remove/lesson=(?P<id_lesson>\d+)/discipline=(?P<id_discipline>\d+)/$', proxy_category.remove_lesson, name="manager_lesson_remove"),
    url(r'^edit/lesson=(?P<id_lesson>\d+)/discipline=(?P<id_discipline>\d+)/$', proxy_category.edit_lesson, name="manager_lesson_edit"),
    url(r'^restore/lesson=(?P<id_lesson>\d+)/discipline=(?P<id_discipline>\d+)/$', proxy_category.restore_lesson, name="manager_lesson_restore"),
)