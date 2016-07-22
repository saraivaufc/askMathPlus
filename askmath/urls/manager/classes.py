from askmath.views.manager import ProxyClasse
from django.conf.urls import patterns, url


proxy_classe = ProxyClasse()  

urlpatterns = patterns('',
    url(r'^view/$', proxy_classe.view_classes, name="manager_classe_view"),
    url(r'^view_removed/$', proxy_classe.view_classes_removed, name="manager_classe_view_removed"),
    url(r'^add/$', proxy_classe.add_classe, name="manager_classe_add"),
    url(r'^remove/classe=(?P<id_classe>\d+)/$', proxy_classe.remove_classe, name="manager_classe_remove"),
    url(r'^edit/classe=(?P<id_classe>\d+)/$', proxy_classe.edit_classe, name="manager_classe_edit"),
    url(r'^restore/classe=(?P<id_classe>\d+)/$', proxy_classe.restore_classe, name="manager_classe_restore"),
)