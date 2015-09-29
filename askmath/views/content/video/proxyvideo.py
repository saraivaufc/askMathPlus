from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from askmath.entities import TextMessage
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

#MODELS
from askmath.models.discipline import Discipline as CategoryModel
from askmath.models.lesson import Lesson as ContactModel
from askmath.models.video import Video as VideoModel

from askmath.views.index import ProxyHome



from .ivideo import IVideo
from .video import Video


class ProxyVideo(IVideo):
    def __init__(self):
        self.__video = Video()
        self.__proxy_home = ProxyHome()
    
    @method_decorator(login_required)
    def view_videos(self, request, id_discipline, id_lesson):
        if request.user.has_perm("askmath.read_video")  and request.user.has_perm("askmath.access_content"):
            try:
                discipline = CategoryModel.objects.filter(id = id_discipline, exists=True,visible=True)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return self.__proxy_home.index(request)
            try:
                lesson = ContactModel.objects.filter(id = id_lesson, exists=True,visible=True)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return self.__proxy_home.index(request)
            try:
                return self.__video.view_videos(request, discipline, lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.__proxy_home.index(request)
    

    @method_decorator(login_required)
    def view_video(self, request, id_video, id_discipline=None, id_lesson=None):
        if request.user.has_perm("askmath.read_video")  and request.user.has_perm("askmath.access_content"):
            try:
                video = VideoModel.objects.filter(id = id_video, exists=True,visible=True)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.VIDEO_NOT_FOUND)
                return self.view_videos(request, id_discipline, id_lesson)
            
            try:
                lesson = ContactModel.objects.filter(id = id_lesson, exists=True,visible=True)[0]
            except Exception, e:
                print e
                try:
                    lesson = video.get_lesson();
                except Exception, e:
                    print e
                    messages.error(request, TextMessage.LESSON_NOT_FOUND)
                    return self.view_videos(request, id_discipline, id_lesson)
            
            try:
                discipline = CategoryModel.objects.filter(id = id_discipline, exists=True,visible=True)[0]
            except Exception, e:
                print e
                try:
                    discipline = lesson.disciplines.filter(exists=True, visible=True)[0]
                except Exception, e:
                    print e
                    messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                    return self.view_videos(request, id_discipline, id_lesson)
            
            
            if not video in lesson.get_videos():
                messages.error(request, TextMessage.VIDEO_NOT_FOUND_IN_LESSON)
                return self.view_videos(request, id_discipline, id_lesson)

            try:
                return self.__video.view_video(request, discipline, lesson, video)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.__proxy_home.index(request)