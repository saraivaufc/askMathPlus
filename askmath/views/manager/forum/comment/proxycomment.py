from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.entities import Message, TextMessage, TypeMessage
from askmath.models import Category as CategoryModel
from askmath.models import Topic as TopicModel
from askmath.models import Comment as CommentModel

from .icomment import IComment
from .comment import Comment
from ..category import ProxyCategory
from ..topic import ProxyTopic

class ProxyComment(IComment):
    def __init__(self):
        self.__comment = Comment()
        self.__proxy_category = ProxyCategory()
        self.__proxy_topic = ProxyTopic()
    
    def remove_comment(self, request, id_category, id_topic, id_comment, message=None):
        if request.user.has_perm("askmath.write_comment")  and request.user.has_perm("askmath.access_manager"):
            try:
                category = CategoryModel.objects.get(id = id_category)
            except:
                message = Message(TextMessage.CATEGORY_NOT_FOUND, TypeMessage.ERROR)
                return self.__proxy_category.view_categories(request, message)
            
            try:
                topic = TopicModel.objects.filter(exists=True, id=id_topic)[0]
            except:
                message = Message(TextMessage.TOPIC_NOT_FOUND, TypeMessage.ERROR)
                return self.__proxy_category.view_category(request, id_category, message)
            
            try:
                comment = CommentModel.objects.filter(exists=True, id=id_comment)[0]
            except:
                message = Message(TextMessage.COMMENT_NOT_FOUND, TypeMessage.ERROR)
                return self.__proxy_topic.view_topic(request, id_category, id_topic, message)
            
            try:
                return self.__comment.remove_comment(request, category,topic, comment, message)
            except:
                message = Message(TextMessage.COMMENT_ERROR_REM, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.__proxy_topic.view_topic(request, id_category, id_topic, message)
    
    def edit_comment(self):
        pass