from django.conf.urls import patterns, url
from .views import DisciplineList, LessonList

urlpatterns = patterns(
    'askmath.api.views',
    url(r'^disciplines/$', DisciplineList.as_view(), name='api_disciplines'),
    url(r'^lessons/$', LessonList.as_view(), name='api_lessons'),
)