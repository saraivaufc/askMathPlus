from django.conf.urls import patterns, include, url
from askmath.views.manager import ProxyPerson

proxy_account = ProxyPerson()  

urlpatterns = patterns('',
    url(r'^choose_person_types/$', proxy_account.choose_person_types, name="manager_person_choose_person_types"),
    url(r'^view/person_type=(?P<PERSONTYPE>\w+)/$', proxy_account.view_persons, name="manager_person_view"),
    url(r'^view_removed/person_type=(?P<PERSONTYPE>\w+)/$', proxy_account.view_persons_removed, name="manager_person_view_removed"),
    url(r'^add/person_type=(?P<PERSONTYPE>\w+)/$', proxy_account.add_person, name="manager_person_add"),
    url(r'^remove/person_type=(?P<PERSONTYPE>\w+)/person=(?P<id_person>\d+)/$', proxy_account.remove_person, name="manager_person_remove"),
    url(r'^remove_registerkey/person_type=(?P<PERSONTYPE>\w+)/registerkey=(?P<id_registerkey>\d+)/$', proxy_account.remove_registerkey, name="manager_person_remove_registerkey"),
    url(r'^restore/person_type=(?P<PERSONTYPE>\w+)/person=(?P<id_person>\d+)/$', proxy_account.restore_person, name="manager_person_remove"),
)