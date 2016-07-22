from askmath.entities import TextMessage
from askmath.models.category import Category as CategoryModel
from askmath.models.topic import Topic as TopicModel
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.utils.decorators import method_decorator
from .itopic import ITopic
from .topic import Topic
from ..category import ProxyCategory


class ProxyTopic(ITopic):
    def __init__(self):
        self.__topic = Topic()
        self.__proxy_category = ProxyCategory()

    def view_topics(self, request, id_category):
        try:
            category = CategoryModel.objects.get(id = id_category)
        except Exception, e:
            print e
            messages.error(request, TextMessage.CATEGORY_NOT_FOUND)
            return self.__proxy_category.view_categories(request)
        try:
            return self.__topic.view_topics(request, category)
        except Exception, e:
            print e
            messages.error(request, TextMessage.ERROR)
        return self.__proxy_category.view_categories(request)
    
    @method_decorator(login_required)
    def view_topics_removed(self, request, id_category):
        if request.user.has_perm("askmath.read_topic")  and request.user.has_perm("askmath.access_forum_admin"):
            try:
                category = CategoryModel.objects.get(id = id_category)
            except Exception, e:
                print e
                messages.error(request, TextMessage.CATEGORY_NOT_FOUND)
                return self.view_topics(request,id_category)
            try:
                return self.__topic.view_topics_removed(request, category)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_topics(request,id_category)
    
    def view_topic(self, request, id_category, id_topic):
        try:
            category = CategoryModel.objects.get(id = id_category)
        except Exception, e:
            print e
            messages.error(request, TextMessage.CATEGORY_NOT_FOUND)
            return self.view_topics(request,id_category)
        
        try:
            topic = TopicModel.objects.filter(exists=True, id=id_topic)[0]
        except Exception, e:
            messages.error(request, TextMessage.TOPIC_NOT_FOUND)
            return self.view_topics(request,id_category)
        
        try:
            return self.__topic.view_topic(request, category, topic)
        except Exception, e:
            messages.error(request, TextMessage.ERROR)
        return self.view_topics(request,id_category)
    def view_topic_removed(self, request, id_category, id_topic):
        try:
            category = CategoryModel.objects.get(id = id_category)
        except Exception, e:
            print e
            messages.error(request, TextMessage.CATEGORY_NOT_FOUND)
            return self.view_topics(request,id_category)
        
        try:
            topic = TopicModel.objects.filter(exists=True, id=id_topic)[0]
        except Exception, e:
            messages.error(request, TextMessage.TOPIC_NOT_FOUND)
            return self.view_topics(request,id_category)
        
        try:
            return self.__topic.view_topic_removed(request, category, topic)
        except Exception, e:
            messages.error(request, TextMessage.ERROR)
        return self.view_topics(request,id_category)

    @method_decorator(login_required)
    def add_topic(self, request,id_category):
        if request.user.has_perm("askmath.write_topic"):
            try:
                category = CategoryModel.objects.filter(exists=True, id=id_category)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.CATEGORY_NOT_FOUND)
                return self.view_topics(request,id_category)
            try:
                return self.__topic.add_topic(request, category)
            except Exception, e:
                print e
                messages.error(request, TextMessage.TOPIC_ERROR_ADD)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_topics(request,id_category)
    
    @method_decorator(login_required)
    def edit_topic(self, request, id_category, id_topic):
        if request.user.has_perm("askmath.write_topic"):
            try:
                category = CategoryModel.objects.filter(exists=True, id=id_category)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.CATEGORY_NOT_FOUND)
                return self.view_topics(request,id_category)
            
            try:
                topic = TopicModel.objects.filter(exists=True, id=id_topic)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.TOPIC_NOT_FOUND)
                return self.view_topics(request,id_category)
            if topic.person == request.user:
                try:
                    return self.__topic.edit_topic(request, category,topic)
                except Exception, e:
                    print e
                    messages.error(request, TextMessage.TOPIC_ERROR_EDIT)
            else:
                messages.error(request, TextMessage.USER_NOT_PERMISSION)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_topics(request,id_category)
    
    @method_decorator(login_required)
    def remove_topic(self, request, id_category, id_topic):
        if request.user.has_perm("askmath.write_topic"):
            try:
                category = CategoryModel.objects.filter(exists=True, id=id_category)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.CATEGORY_NOT_FOUND)
                return self.view_topics(request,id_category)
            
            try:
                topic = TopicModel.objects.filter(exists=True, id=id_topic)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.TOPIC_NOT_FOUND)
                return self.view_topics(request,id_category)
            
            if topic.person == request.user or request.user.has_perm("askmath.access_forum_admin"):
                try:
                    return self.__topic.remove_topic(request, category, topic)
                except Exception, e:
                    print e
                    messages.error(request, TextMessage.TOPIC_ERROR_REM)
            else:
                messages.error(request, TextMessage.USER_NOT_PERMISSION)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_topics(request,id_category)
    
    @method_decorator(login_required)
    def restore_topic(self, request, id_category, id_topic):
        if request.user.has_perm("askmath.write_topic"):
            try:
                category = CategoryModel.objects.filter(exists=True, id=id_category)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.CATEGORY_NOT_FOUND)
                return self.view_topics(request,id_category)
            
            try:
                topic = TopicModel.objects.filter(id=id_topic)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.TOPIC_NOT_FOUND)
                return self.view_topics(request,id_category)
            
            if topic.person == request.user or request.user.has_perm("askmath.access_forum_admin"):
                try:
                    return self.__topic.restore_topic(request, category, topic)
                except Exception, e:
                    print e
                    messages.error(request, TextMessage.TOPIC_ERROR_REM)
            else:
                messages.error(request, TextMessage.USER_NOT_PERMISSION)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_topics(request,id_category)
    
    @method_decorator(login_required)
    def like_topic(self, request, id_topic):
        if request.user.has_perm("askmath.read_topic"):
            try:
                topic = TopicModel.objects.filter(exists=True, id=id_topic)[0]
            except Exception, e:
                print e 
                return HttpResponse("False")
            try:
                return self.__topic.like_topic(request,topic)
            except Exception, e:
                print e
        return HttpResponse("False")
    
    @method_decorator(login_required)
    def unlike_topic(self, request,id_topic):
        if request.user.has_perm("askmath.read_topic"):
            try:
                topic = TopicModel.objects.filter(exists=True, id=id_topic)[0]
            except Exception, e:
                print e
                return HttpResponse("False")
            try:
                return self.__topic.unlike_topic(request, topic)
            except Exception, e:
                print e
        return HttpResponse("False")