from django.conf.urls import patterns, include, url
from askmath.views.manager import ProxyPerson

proxy_person = ProxyPerson()  

urlpatterns = patterns('',
    url(r'^choose_person_types/$', proxy_person.choose_person_types),
    url(r'^view/person_type=(?P<PERSONTYPE>\w+)/$', proxy_person.view_persons),
    url(r'^view_removed/person_type=(?P<PERSONTYPE>\w+)/$', proxy_person.view_persons_removed),
    url(r'^view/person_type=(?P<PERSONTYPE>\w+)/person=(?P<id_person>\d+)/$', proxy_person.view_person),
    url(r'^add/person_type=(?P<PERSONTYPE>\w+)/$', proxy_person.add_person),
    url(r'^remove/person_type=(?P<PERSONTYPE>\w+)/person=(?P<id_person>\d+)/$', proxy_person.remove_person),
    url(r'^restore/person_type=(?P<PERSONTYPE>\w+)/person=(?P<id_person>\d+)/$', proxy_person.restore_person),
)