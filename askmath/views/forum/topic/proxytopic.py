from askmath.entities import Message, TextMessage, TypeMessage
from askmath.models.category import Category as CategoryModel
from askmath.models.topic import Topic as TopicModel
from .itopic import ITopic
from .topic import Topic
from ..category import ProxyCategory
from django.http.response import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class ProxyTopic(ITopic):
    def __init__(self):
        self.__topic = Topic()
        self.__proxy_category = ProxyCategory()
    
    @method_decorator(login_required)
    def view_topic(self, request, id_category, id_topic, message=None):
        if request.user.has_perm("askmath.read_topic"):
            try:
                category = CategoryModel.objects.get(id = id_category)
            except:
                message = Message(TextMessage.CATEGORY_NOT_FOUND, TypeMessage.ERROR)
                return self.view_categories(request, message)
            
            try:
                topic = TopicModel.objects.filter(exists=True, id=id_topic)[0]
            except:
                message = Message(TextMessage.TOPIC_NOT_FOUND, TypeMessage.ERROR)
                return self.__proxy_category.view_category(request, id_category, message)
            
            try:
                return self.__topic.view_topic(request, category, topic, message)
            except:
                message = Message(TextMessage.ERROR_FORM, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.__proxy_category.view_category(request, id_category, message)
    
    @method_decorator(login_required)
    def add_topic(self, request,id_category, message=None):
        if request.user.has_perm("askmath.write_topic"):
            try:
                category = CategoryModel.objects.filter(exists=True, id=id_category)[0]
            except:
                message = Message(TextMessage.CATEGORY_NOT_FOUND, TypeMessage.ERROR)
                return self.__proxy_category.view_category(request, id_category, message)
            #try:
            return self.__topic.add_topic(request, category, message)
            #except:
            #    message = Message(TextMessage.TOPIC_ERROR_ADD, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.__proxy_category.view_category(request, id_category, message)
    
    @method_decorator(login_required)
    def edit_topic(self, request, id_category, id_topic, message=None):
        if request.user.has_perm("askmath.write_topic"):
            try:
                category = CategoryModel.objects.filter(exists=True, id=id_category)[0]
            except:
                message = Message(TextMessage.CATEGORY_NOT_FOUND, TypeMessage.ERROR)
                return self.__proxy_category.view_category(request, id_category, message)
            
            try:
                topic = TopicModel.objects.filter(exists=True, id=id_topic)[0]
            except:
                message = Message(TextMessage.TOPIC_NOT_FOUND, TypeMessage.ERROR)
                return self.__proxy_category.view_category(request, id_category, message)
            if topic.person == request.user:
                try:
                    return self.__topic.edit_topic(request, category,topic,  message)
                except:
                    message = Message(TextMessage.TOPIC_ERROR_EDIT, TypeMessage.ERROR)
            else:
                message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.__proxy_category.view_category(request, id_category, message)
    
    @method_decorator(login_required)
    def remove_topic(self, request, id_category, id_topic, message=None):
        if request.user.has_perm("askmath.write_topic"):
            try:
                category = CategoryModel.objects.filter(exists=True, id=id_category)[0]
            except:
                message = Message(TextMessage.CATEGORY_NOT_FOUND, TypeMessage.ERROR)
                return self.__proxy_category.view_category(request, id_category, message)
            
            try:
                topic = TopicModel.objects.filter(exists=True, id=id_topic)[0]
            except:
                message = Message(TextMessage.TOPIC_NOT_FOUND, TypeMessage.ERROR)
                return self.__proxy_category.view_category(request, id_category, message)
            
            if topic.person == request.user or request.user.has_perm("askmath.access_forum_admin"):
                try:
                    return self.__topic.remove_topic(request, category, topic, message)
                except:
                    message = Message(TextMessage.TOPIC_ERROR_REM, TypeMessage.ERROR)
            else:
                message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.__proxy_category.view_category(request, id_category, message)
    
    @method_decorator(login_required)
    def restore_topic(self):
        pass
    
    @method_decorator(login_required)
    def like_topic(self, request, id_topic, message=None):
        if request.user.has_perm("askmath.read_topic"):
            try:
                topic = TopicModel.objects.filter(exists=True, id=id_topic)[0]
            except:
                return HttpResponse("False")
            try:
                return self.__topic.like_topic(request,topic, message)
            except:
                pass
        return HttpResponse("False")
    
    @method_decorator(login_required)
    def unlike_topic(self, request,id_topic, message=None):
        if request.user.has_perm("askmath.read_topic"):
            try:
                topic = TopicModel.objects.filter(exists=True, id=id_topic)[0]
            except:
                return HttpResponse("False")
            try:
                return self.__topic.unlike_topic(request, topic, message)
            except:
                pass
        return HttpResponse("False")