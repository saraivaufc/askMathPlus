from .icomment import IComment
from askmath.models import Comment as CommentModel
from django.template import Context, Template
from django.http.response import HttpResponse, HttpResponseRedirect
import json
from askmath.forms import CommentForm
from ..category import ProxyCategory
from ..topic import ProxyTopic
from askmath.entities import TextMessage
from django.contrib import messages
class Comment(IComment):
    def __init__(self):
        self.__proxy_category = ProxyCategory()
        self.__proxy_topic = ProxyTopic()


    def add_comment(self, request, category, topic):
        if request.method == 'POST':
            request.POST = request.POST.copy()
            request.POST['person'] = request.user.id
            request.POST['topic'] = topic.id
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save()
                url = "/forum/topics/view/category=%d/topic=%d/#comment-%d" % (category.id, topic.id, comment.id)
                return HttpResponseRedirect(url)
            else:
                messages.error(request, TextMessage.COMMENT_ERROR_ADD)
        return self.__proxy_topic.view_topic(request, category.id, topic.id)
        
    def remove_comment(self, request, category, topic, comment):
        comment.delete()
        url = "/forum/topics/view/category=%d/topic=%d/" % (category.id, topic.id)
        return HttpResponseRedirect(url)
        
    def edit_comment(self, request, category, topic, comment):
        if request.method == 'POST':
            request.POST = request.POST.copy()
            request.POST['person'] = request.user.id
            request.POST['topic'] = topic.id
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                comment = form.save()
                return HttpResponse(json.dumps({'result':'True','value': comment.get_description() }))
            else:
                return HttpResponse(json.dumps({'result':'False'}))
        else:
            return HttpResponse(json.dumps({'result':'False'}))
            
    
    def like_comment(self, request, comment):
        if request.user in comment.get_likes_persons():
            return HttpResponse(json.dumps({'result':'False'}))
        elif comment.like(request.user):
            return HttpResponse(json.dumps({'result':'True','value':len(comment.get_likes())}))
        else:
            return HttpResponse(json.dumps({'result':'False'}))
    
    def unlike_comment(self, request, comment):
        if not request.user in comment.get_likes_persons():
            return HttpResponse(json.dumps({'result':'False'}))
        elif comment.unlike(request.user):
            return HttpResponse(json.dumps({'result':'True','value':len(comment.get_likes())}))
        else:
            return HttpResponse(json.dumps({'result':'False'}))