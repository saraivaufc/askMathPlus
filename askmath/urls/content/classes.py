from django.conf.urls import patterns, include, url

from askmath.views.content import ProxyClasse


proxy_classe = ProxyClasse()  

urlpatterns = patterns('',
    url(r'^$', proxy_classe.view_classes),
    url(r'^view/$', proxy_classe.view_classes),
    url(r'^view/classe=(?P<id_classe>\d+)/$', proxy_classe.view_classe),
    url(r'^set_current/classe=(?P<id_classe>\d+)/$', proxy_classe.set_current),
    url(r'^join_classe/classe=(?P<id_classe>\d+)/$', proxy_classe.join_classe),
    url(r'^out_classe/classe=(?P<id_classe>\d+)/$', proxy_classe.out_classe),
)