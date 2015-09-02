from .itopic import ITopic
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.entities import Message, TextMessage, TypeMessage
from askmath.forms import TopicForm, CommentForm
from ..category import ProxyCategory
import json

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
                message = Message(TextMessage.COMMENT_SUCCESS_ADD, TypeMessage.SUCCESS)
                request.method = "GET"
                url = "/forum/topics/view/category=%d/topic=%d/" % (category.id, topic.id)
                return HttpResponseRedirect(url)
        else:
            form = CommentForm()
        return render(request, "askmath/forum/topic/view_topic.html",
            {'request':request,'category': category,'topic': topic,'form': form,'message': message})
    
    def add_topic(self, request, category, message=None):
        if request.method == "POST":
            request.POST = request.POST.copy()
            request.POST['category']=category.id
            request.POST['person'] = request.user.id
            form = TopicForm(request.POST, request.FILES)
            if form.is_valid():
                topic = form.save()
                url = "/forum/categories/view/category=%d/" % (category.id)
                return HttpResponseRedirect(url)
            else:
                message = Message(TextMessage.ERROR_FORM, TypeMessage.ERROR)
                return self.__proxy_category.view_category(request, category, message)
        else:
            form = TopicForm()
            return render(request, "askmath/forum/topic/form_topic.html", 
            {'request':request,'form': form,'category': category, 'title_form':_('Add Topic'), 'message': message})

    def edit_topic(self, request, category, topic, message=None):
        if request.method == 'POST':
            request.POST = request.POST.copy()
            request.POST['category']=category.id
            request.POST['person'] = request.user.id
            form = TopicForm(request.POST, request.FILES, instance = topic)
            if form.is_valid():
                topic=form.save()
                url = "/forum/topics/view/category=%d/topic=%d/" % (category.id, topic.id)
                return HttpResponseRedirect(url)
            else:
                message = Message(TextMessage.ERROR_FORM, TypeMessage.ERROR)
        else:
            form = TopicForm( instance = topic)
        return render(request, "askmath/forum/topic/form_topic.html", 
            {'request':request,'form': form,'category': category,'topic': topic, 'title_form':_('Edit Topic'), 'message': message})
    
    def remove_topic(self, request, category, topic, message=None):
        topic.delete()
        url = "/forum/categories/view/category=%d/" % (category.id)
        return HttpResponseRedirect(url)
    
    def restore_topic(self):
        pass
    
    def like_topic(self, request, topic, message=None):
        if request.user in topic.get_likes_persons():
            return HttpResponse("False")
        elif topic.like(request.user):
            return HttpResponse(json.dumps({'result':'True','value':len(topic.get_likes())}))
        else:
            return HttpResponse("False")
    
    def unlike_topic(self, request, topic, message=None):
        if not request.user in topic.get_likes_persons():
            return HttpResponse("False")
        elif topic.unlike(request.user):
            return HttpResponse(json.dumps({'result':'True','value':len(topic.get_likes())}))
        else:
            return HttpResponse("False")