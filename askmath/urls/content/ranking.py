from askmath.views.content import ProxyRanking
from django.conf.urls import patterns, url

proxy_ranking = ProxyRanking()

urlpatterns = patterns('',
	url(r'^$', proxy_ranking.view_ranking, name="content_ranking_view"),
	
	url(r'^view/$', proxy_ranking.view_ranking, name="content_ranking_view"),
	url(r'^view/classe=(?P<id_classe>\d+)/$', proxy_ranking.view_ranking, name="content_ranking_view"),
)
