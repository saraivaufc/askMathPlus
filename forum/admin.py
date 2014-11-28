from django.contrib import admin

from forum.models import Forum, Thread, Post

class ForumAdmin(admin.ModelAdmin):
    list_display = ('title', '_parents_repr', 'ordering', )
    list_filter = ('groups', )
    ordering = ['ordering', 'parent', 'title', ]
    prepopulated_fields = {'slug': ('title', )}
    search_fields = ('id', 'title', )

class ThreadAdmin(admin.ModelAdmin):
    list_display = ('title', 'forum', 'latest_post_time', )
    list_filter = ('forum', 'sticky', 'closed', 'latest_post_time', )
    search_fields = ('id', 'title', )

class PostAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'thread', 'author', 'time', )
    list_filter = ('time', )
    search_fields = ('id', )

admin.site.register(Forum, ForumAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Post, PostAdmin)
