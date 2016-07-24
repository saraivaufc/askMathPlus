import json

from askmath.entities import TextMessage
from askmath.models import Category as CategoryModel
from askmath.models import Comment as CommentModel
from askmath.models import Topic as TopicModel
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from .comment import Comment
from .icomment import IComment


class ProxyComment(IComment):
    def __init__(self):
        self.__comment = Comment()

    @method_decorator(login_required)
    def add_comment(self, request, id_category, id_topic, message=None):
        if request.user.has_perm("askmath.write_comment") or request.user.has_perm("askmath.access_forum_admin"):
            try:
                category = CategoryModel.objects.filter(exists=True, id=id_category)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.CATEGORY_NOT_FOUND)
                return HttpResponseRedirect(reverse('askmath:forum_category_view'))

            try:
                topic = TopicModel.objects.filter(exists=True, id=id_topic)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.TOPIC_NOT_FOUND)
                return HttpResponseRedirect(reverse('askmath:forum_topic_view', kwargs={'id_category': id_category}))

            try:
                return self.__comment.add_comment(request, category, topic)
            except Exception, e:
                print e
                messages.error(request, TextMessage.COMMENT_ERROR_ADD)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)

        return HttpResponseRedirect(
            reverse('askmath:forum_topic_view', kwargs={'id_category': id_category, 'id_topic': id_topic}))

    @method_decorator(login_required)
    def remove_comment(self, request, id_category, id_topic, id_comment):
        if request.user.has_perm("askmath.write_comment") or request.user.has_perm("askmath.access_forum_admin"):
            try:
                category = CategoryModel.objects.filter(exists=True, id=id_category)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.CATEGORY_NOT_FOUND)
                return HttpResponseRedirect(reverse('askmath:forum_category_view'))

            try:
                topic = TopicModel.objects.filter(exists=True, id=id_topic)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.TOPIC_NOT_FOUND)
                return HttpResponseRedirect(reverse('askmath:forum_topic_view', kwargs={'id_category': id_category}))

            try:
                comment = CommentModel.objects.filter(exists=True, id=id_comment)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.COMMENT_NOT_FOUND)
                return HttpResponseRedirect(
                    reverse('askmath:forum_topic_view', kwargs={'id_category': id_category, 'id_topic': id_topic}))

            try:
                return self.__comment.remove_comment(request, category, topic, comment)
            except Exception, e:
                print e
                messages.error(request, TextMessage.COMMENT_ERROR_REM)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)

        return HttpResponseRedirect(
            reverse('askmath:forum_topic_view', kwargs={'id_category': id_category, 'id_topic': id_topic}))

    @method_decorator(login_required)
    def edit_comment(self, request, id_category, id_topic, id_comment):
        if request.user.has_perm("askmath.write_comment") or request.user.has_perm("askmath.access_forum_admin"):
            try:
                category = CategoryModel.objects.filter(exists=True, id=id_category)[0]
            except Exception, e:
                print e
                return HttpResponse(json.dumps({'result': 'False'}))

            try:
                topic = TopicModel.objects.filter(exists=True, id=id_topic)[0]
            except Exception, e:
                print e
                return HttpResponse(json.dumps({'result': 'False'}))

            try:
                comment = CommentModel.objects.filter(exists=True, id=id_comment)[0]
            except Exception, e:
                print e
                return HttpResponse(json.dumps({'result': 'False'}))

            try:
                return self.__comment.edit_comment(request, category, topic, comment)
            except Exception, e:
                print e
                return HttpResponse(json.dumps({'result': 'False'}))
        else:
            return HttpResponse(json.dumps({'result': 'False'}))

    @method_decorator(login_required)
    def like_comment(self, request, id_comment):
        if request.user.has_perm("askmath.write_comment") or request.user.has_perm("askmath.access_forum_admin"):
            try:
                comment = CommentModel.objects.filter(exists=True, id=id_comment)[0]
            except Exception, e:
                print e
                return HttpResponse(json.dumps({'result': 'False'}))
            try:
                return self.__comment.like_comment(request, comment)
            except Exception, e:
                print e
                return HttpResponse(json.dumps({'result': 'False'}))

    @method_decorator(login_required)
    def unlike_comment(self, request, id_comment):
        if request.user.has_perm("askmath.write_comment") or request.user.has_perm("askmath.access_forum_admin"):
            try:
                comment = CommentModel.objects.filter(exists=True, id=id_comment)[0]
            except Exception, e:
                print e
                return HttpResponse(json.dumps({'result': 'False'}))
            try:
                return self.__comment.unlike_comment(request, comment)
            except Exception, e:
                print e
                return HttpResponse(json.dumps({'result': 'False'}))
        else:
            return HttpResponse(json.dumps({'result': 'False'}))
