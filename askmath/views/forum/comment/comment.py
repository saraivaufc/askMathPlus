from .icomment import IComment
from askmath.models import Comment as CommentModel
from django.template import Context, Template
from django.http.response import HttpResponse
import json
from ..category import ProxyCategory
from ..topic import ProxyTopic

from askmath.entities import Message, TextMessage, TypeMessage
class Comment(IComment):
    def __init__(self):
        self.__proxy_category = ProxyCategory()
        self.__proxy_topic = ProxyTopic()
        
    def remove_comment(self, request, category, topic, comment, message=None):
        comment.delete()
        message = Message(TextMessage.COMMENT_SUCCESS_REM, TypeMessage.SUCCESS)
        return self.__proxy_topic.view_topic(request, category.id, topic.id, message)
    
    def edit_comment(self):
        pass
    
    def like_comment(self, request, comment, message=None):
        print "Plaa"
        if request.user in comment.get_likes_persons():
            return HttpResponse("False")
        elif comment.like(request.user):
            return HttpResponse(json.dumps({'result':'True','value':len(comment.get_likes())}))
        else:
            return HttpResponse("False")
    
    def unlike_comment(self, request, comment, message=None):
        if not request.user in comment.get_likes_persons():
            return HttpResponse("False")
        elif comment.unlike(request.user):
            return HttpResponse(json.dumps({'result':'True','value':len(comment.get_likes())}))
        else:
            return HttpResponse("False")