from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.entities import Message, TextMessage, TypeMessage
from askmath.models import Category as CategoryModel
from askmath.models import Topic as TopicModel
from .icomment import IComment
from .comment import Comment
from ..category import ProxyCategory

class ProxyComment(IComment):
    def __init__(self):
        self.__comment = Comment()
        self.__proxy_category = ProxyCategory()
        
    def add_comment(self, request, id_category, id_topic, comment, message=None):
        if request.user.has_perm("askmath.write_comment")  and request.user.has_perm("askmath.access_manager"):
            try:
                category = CategoryModel.objects.filter(exists=True, id=id_category)[0]
            except:
                message = Message(TextMessage.CATEGORY_NOT_FOUND, TypeMessage.ERROR)
                return HttpResponse("")
            try:
                topic = TopicModel.objects.filter(exists=True, id=id_topic)[0]
            except:
                message = Message(TextMessage.TOPIC_NOT_FOUND, TypeMessage.ERROR)
                return HttpResponse("")
            try:
                return self.__comment.add_comment(request, category, topic, comment, message)
            except:
                message = Message(TextMessage.COMMENT_ERROR_ADD, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return HttpResponse("")
    
    def remove_comment(self):
        pass
    
    def edit_comment(self):
        pass