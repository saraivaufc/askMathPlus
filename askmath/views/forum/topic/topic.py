from .itopic import ITopic
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.entities import TextMessage
from django.contrib import messages
from askmath.forms import TopicForm, CommentForm
from ..category import ProxyCategory
import json

class Topic(ITopic):
    def __init__(self):
        self.__proxy_category = ProxyCategory()
        
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
                url = "/forum/categories/view/category=%d/" % (category.id)
                return HttpResponseRedirect(url)
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
                url = "/forum/topics/view/category=%d/topic=%d/" % (category.id, topic.id)
                return HttpResponseRedirect(url)
            else:
                messages.error(request, TextMessage.ERROR_FORM)
        else:
            form = TopicForm( instance = topic)
        return render(request, "askmath/forum/topic/form_topic.html", 
            {'request':request,'form': form,'category': category,'topic': topic, 'title_form':_('Edit Topic')})
    
    def remove_topic(self, request, category, topic):
        topic.delete()
        url = "/forum/categories/view/category=%d/" % (category.id)
        return HttpResponseRedirect(url)
    
    def restore_topic(self):
        pass
    
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