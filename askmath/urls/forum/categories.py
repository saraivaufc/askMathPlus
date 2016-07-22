from askmath.views.forum import ProxyCategory
from django.conf.urls import patterns, url

proxy_category = ProxyCategory()

urlpatterns = patterns('',
                       url(r'^$', proxy_category.view_categories),

                       url(r'^view/$', proxy_category.view_categories, name="forum_category_view"),
                       url(r'^view_removed/$', proxy_category.view_categories_removed,
                           name="forum_category_view_removed"),
                       url(r'^add/$', proxy_category.add_category, name="forum_category_add"),
                       url(r'^remove/category=(?P<id_category>\d+)/$', proxy_category.remove_category,
                           name="forum_category_remove"),
                       url(r'^edit/category=(?P<id_category>\d+)/$', proxy_category.edit_category,
                           name="forum_category_edit"),
                       url(r'^restore/category=(?P<id_category>\d+)/$', proxy_category.restore_category,
                           name="forum_category_restore"),
                       )
