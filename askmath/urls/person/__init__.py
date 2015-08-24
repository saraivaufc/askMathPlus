from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'account/', include('askmath.urls.person.account')),
)