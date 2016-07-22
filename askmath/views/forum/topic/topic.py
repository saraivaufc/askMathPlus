import json

from askmath.entities import TextMessage
from askmath.forms import TopicForm, CommentForm
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from .itopic import ITopic
from ..category import ProxyCategory


class Topic(ITopic):
    def __init__(self):
        self.__proxy_category = ProxyCategory()
        
    def view_topics(self, request, category):
        topics = category.get_topics()
        return render(request, "askmath/forum/topic/view_topics.html", 
            {'request':request,'category': category,'topics':topics})
    
    def view_topics_removed(self, request, category):
        topics = category.get_topics_removed()
        return render(request, "askmath/forum/topic/view_topics.html", 
            {'request':request,'category': category,'topics':topics,'is_removed':True})

    def view_topic(self, request, category, topic):
        form = CommentForm()
        return render(request, "askmath/forum/topic/view_topic.html",
            {'request':request,'category': category,'topic': topic,'form': form})

    def add_topic(self, request, category):
        if request.method == "POST":
            request.POST = request.POST.copy()
            request.POST['category']=category.id
            request.POST['person'] = request.user.id
            form = TopicForm(request.POST, request.FILES)
            if form.is_valid():
                topic = form.save()
                messages.success(request, TextMessage.TOPIC_SUCCESS_ADD)
                return self.view_topics(request, category)
            else:
                messages.error(request, TextMessage.ERROR_FORM)
        else:
            form = TopicForm()
        return render(request, "askmath/forum/topic/form_topic.html", 
        {'request':request,'form': form,'category': category, 'title_form':_('Add Topic')})

    def edit_topic(self, request, category, topic):
        if request.method == 'POST':
            request.POST = request.POST.copy()
            request.POST['category']=category.id
            request.POST['person'] = request.user.id
            form = TopicForm(request.POST, request.FILES, instance = topic)
            if form.is_valid():
                topic=form.save()
                messages.success(request, TextMessage.TOPIC_SUCCESS_EDIT)
                return self.view_topic(request, category, topic)
            else:
                messages.error(request, TextMessage.ERROR_FORM)
        else:
            form = TopicForm( instance = topic)
        return render(request, "askmath/forum/topic/form_topic.html", 
            {'request':request,'form': form,'category': category,'topic': topic, 'title_form':_('Edit Topic')})
    
    def remove_topic(self, request, category, topic):
        topic.delete()
        messages.success(request, TextMessage.TOPIC_SUCCESS_REM)
        return self.view_topics(request, category)
    
    def restore_topic(self, request, category, topic):
        topic.restore()
        messages.success(request, TextMessage.TOPIC_SUCCESS_RESTORE)
        return self.view_topics(request, category)
    
    def like_topic(self, request, topic):
        if request.user in topic.get_likes_persons():
            return HttpResponse(json.dumps({'result':'False','value':len(topic.get_likes())}))
        elif topic.like(request.user):
            return HttpResponse(json.dumps({'result':'True','value':len(topic.get_likes())}))
        else:
            return HttpResponse(json.dumps({'result':'False','value':len(topic.get_likes())}))
    
    def unlike_topic(self, request, topic):
        if not request.user in topic.get_likes_persons():
            return HttpResponse(json.dumps({'result':'False','value':len(topic.get_likes())}))
        elif topic.unlike(request.user):
            return HttpResponse(json.dumps({'result':'True','value':len(topic.get_likes())}))
        else:
            return HttpResponse(json.dumps({'result':'False','value':len(topic.get_likes())}))