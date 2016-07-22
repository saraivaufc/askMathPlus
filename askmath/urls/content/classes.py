from askmath.views.content import ProxyClasse
from django.conf.urls import patterns, url

proxy_classe = ProxyClasse()

urlpatterns = patterns('',
                       url(r'^$', proxy_classe.view_classes),

                       url(r'^view/$', proxy_classe.view_classes, name="content_classe_view"),
                       url(r'^view/classe=(?P<id_classe>\d+)/$', proxy_classe.view_classe, name="content_classe_view"),
                       url(r'^set_current/classe=(?P<id_classe>\d+)/$', proxy_classe.set_current,
                           name="content_classe_set_current"),
                       url(r'^join_classe/classe=(?P<id_classe>\d+)/$', proxy_classe.join_classe,
                           name="content_classe_join_classe"),
                       url(r'^out_classe/classe=(?P<id_classe>\d+)/$', proxy_classe.out_classe,
                           name="content_classe_out_classe"),
                       )
