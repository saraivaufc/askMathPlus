from django.conf.urls import patterns, include, url

from askmath.views.manager import ProxyClasse


proxy_classe = ProxyClasse()  

urlpatterns = patterns('',
    url(r'^view/$', proxy_classe.view_classes),
    url(r'^view_removed/$', proxy_classe.view_classes_removed),
    url(r'^add/$', proxy_classe.add_classe),
    url(r'^remove/classe=(?P<id_classe>\d+)/$', proxy_classe.remove_classe),
    url(r'^edit/classe=(?P<id_classe>\d+)/$', proxy_classe.edit_classe),
    url(r'^restore/classe=(?P<id_classe>\d+)/$', proxy_classe.restore_classe),
)