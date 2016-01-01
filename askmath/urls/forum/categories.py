from django.conf.urls import patterns, include, url

from askmath.views.forum import ProxyCategory


proxy_category = ProxyCategory()

urlpatterns = patterns('',
    url(r'^$', proxy_category.view_categories),
    url(r'^view/$', proxy_category.view_categories),
    url(r'^view_removed/$', proxy_category.view_categories_removed),
    url(r'^add/$', proxy_category.add_category),
    url(r'^remove/category=(?P<id_category>\d+)/$', proxy_category.remove_category),
    url(r'^edit/category=(?P<id_category>\d+)/$', proxy_category.edit_category),
    url(r'^restore/category=(?P<id_category>\d+)/$', proxy_category.restore_category),
)