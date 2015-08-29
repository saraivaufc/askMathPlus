from .itopic import ITopic
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.entities import Message, TextMessage, TypeMessage
from askmath.forms import TopicForm, CommentForm
from ..category import ProxyCategory

class Topic(ITopic):
    def __init__(self):
        self.__proxy_category = ProxyCategory()
        
    def view_topic(self, request, category, topic, message=None):
        if request.method == 'POST':
            request.POST = request.POST.copy()
            request.POST['person'] = request.user.id
            request.POST['topic'] = topic.id
            form = CommentForm(request.POST, request.FILES)
            if form.is_valid():
                comment = form.save()
                message = Message(TextMessage.TOPIC_SUCCESS_ADD, TypeMessage.SUCCESS)
                request.method = "GET"
                return self.view_topic(request, category, topic, message)
        else:
            form = CommentForm()
        return render(request, "askmath/manager/forum/topic/manager_view_topic.html",
            {'request':request,'category': category,'topic': topic,'form': form,'message': message})
    
    def add_topic(self, request, category, message=None):
        if request.method == "POST":
            request.POST = request.POST.copy()
            request.POST['category']=category.id
            request.POST['person'] = request.user.id
            form = TopicForm(request.POST, request.FILES)
            if form.is_valid():
                topic = form.save()
                message = Message(TextMessage.TOPIC_SUCCESS_ADD, TypeMessage.SUCCESS)
                request.method = "GET"
                return self.view_topic(request, category, topic, message)
            else:
                message = Message(TextMessage.ERROR_FORM, TypeMessage.ERROR)
        return self.__proxy_category.view_category(request, category.id, message)
    def edit_topic(self, request, category, topic, message=None):
        if request.method == 'POST':
            request.POST = request.POST.copy()
            request.POST['category']=category.id
            request.POST['person'] = request.user.id
            form = TopicForm(request.POST, request.FILES, instance = topic)
            if form.is_valid():
                topic=form.save()
                message = Message(TextMessage.TOPIC_SUCCESS_EDIT, TypeMessage.SUCCESS)
                request.method = "GET"
                return self.view_topic(request, category, topic, message)
            else:
                message = Message(TextMessage.ERROR_FORM, TypeMessage.ERROR)
        else:
            form = TopicForm( instance = topic)
        return render(request, "askmath/manager/forum/topic/manager_form_topic.html", 
            {'request':request,'form': form,'category': category,'topic': topic, 'title_form':_('Edit Topic'), 'message': message})
    
    def remove_topic(self, request, category, topic, message=None):
        topic.delete()
        message = Message(TextMessage.TOPIC_SUCCESS_REM, TypeMessage.SUCCESS)
        return self.__proxy_category.view_category(request, category.id, message)
    
    def restore_topic(self):
        pass
    
    def like_topic(self):
        pass
    
    def unlike_topic(self):
        pass