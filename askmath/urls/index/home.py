from django.conf.urls import patterns, include, url
from askmath.views.index import ProxyHome
from askmath.feeds import LessonsLatests

proxy_home = ProxyHome()

urlpatterns = patterns('',
    url(r'^$', proxy_home.index),

    url(r'^home/$', proxy_home.index, name="home"),
    url(r'^about/$', proxy_home.about, name="about"),
    url(r'^message/$', proxy_home.message, name="message"),
    url(r'^terms/$', proxy_home.terms, name="terms"),
    url(r'^policies/$', proxy_home.policies, name="policies"),
    url(r'^credits/$', proxy_home.credits, name="credits"),
    url(r'^contents/$', proxy_home.contents, name="contents"),
    url(r'^contents/lesson=(?P<id_lesson>\d+)/$', proxy_home.contents, name="contents"),
    url(r'^feed/$', LessonsLatests(), name="feed"),
)

