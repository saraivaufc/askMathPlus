from .icomment import IComment
from askmath.models import Comment as CommentModel
from django.template import Context, Template
from django.http.response import HttpResponse

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