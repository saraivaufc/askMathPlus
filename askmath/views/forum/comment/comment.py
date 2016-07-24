import json

from askmath.entities import TextMessage
from askmath.forms import CommentForm
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse, HttpResponseRedirect
from .icomment import IComment


class Comment(IComment):

    def add_comment(self, request, category, topic):
        if request.method == 'POST':
            request.POST = request.POST.copy()
            request.POST['person'] = request.user.id
            request.POST['topic'] = topic.id
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save()
                return HttpResponseRedirect(reverse('askmath:forum_topic_view', kwargs={'id_category': category.id, 'id_topic': topic.id}) + "#comment-%d" % (comment.id, ))
            else:
                messages.error(request, TextMessage.COMMENT_ERROR_ADD)
        return HttpResponseRedirect( reverse('askmath:forum_topic_view', kwargs={'id_category': category.id, 'id_topic': topic.id}))

    def remove_comment(self, request, category, topic, comment):
        comment.delete()
        return HttpResponseRedirect(reverse('askmath:forum_topic_view', kwargs={'id_category': category.id,'id_topic': topic.id}))

    def edit_comment(self, request, category, topic, comment):
        if request.method == 'POST':
            request.POST = request.POST.copy()
            request.POST['person'] = request.user.id
            request.POST['topic'] = topic.id
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                comment = form.save()
                return HttpResponse(json.dumps({'result': 'True', 'value': comment.get_description()}))
            else:
                return HttpResponse(json.dumps({'result': 'False'}))
        else:
            return HttpResponse(json.dumps({'result': 'False'}))

    def like_comment(self, request, comment):
        if request.user in comment.get_likes_persons():
            return HttpResponse(json.dumps({'result': 'False'}))
        elif comment.like(request.user):
            return HttpResponse(json.dumps({'result': 'True', 'value': len(comment.get_likes())}))
        else:
            return HttpResponse(json.dumps({'result': 'False'}))

    def unlike_comment(self, request, comment):
        if not request.user in comment.get_likes_persons():
            return HttpResponse(json.dumps({'result': 'False'}))
        elif comment.unlike(request.user):
            return HttpResponse(json.dumps({'result': 'True', 'value': len(comment.get_likes())}))
        else:
            return HttpResponse(json.dumps({'result': 'False'}))
