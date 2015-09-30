from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from askmath.models.lesson import Lesson as ContactModel
from askmath.models.video import Video as VideoModel
from askmath.entities import TextMessage
from django.contrib import messages
from askmath.views.index import ProxyHome

from .ivideo import IVideo
from .video import Video
import json

class ProxyVideo(IVideo):
    
    def __init__(self):
        self.__video = Video()
        self.__proxy_home = ProxyHome()
    
    @method_decorator(login_required)
    def choose_lesson(self, request):
        if request.user.has_perm("askmath.read_video")  and request.user.has_perm("askmath.access_manager"):
            try:
                return self.__video.choose_lesson(request)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.__proxy_home.index(request)
    
    @method_decorator(login_required)
    def view_videos(self, request, id_lesson):
        if request.user.has_perm("askmath.read_video")  and request.user.has_perm("askmath.access_manager"):
            try:
                lesson = ContactModel.objects.get(id = id_lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return self.choose_lesson(request )
            try:
                if lesson:
                    return self.__video.view_videos(request,lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.choose_lesson(request)
    
    @method_decorator(login_required)
    def view_videos_removed(self, request, id_lesson = None):
        if request.user.has_perm("askmath.read_video")  and request.user.has_perm("askmath.access_manager"):
            try:
                lesson = ContactModel.objects.get(id = id_lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return self.choose_lesson(request)
            try:
                if lesson:
                    return self.__video.view_videos_removed(request,lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.choose_lesson(request)
    
    @method_decorator(login_required)
    def view_video(self, request, id_lesson, id_video):
        if request.user.has_perm("askmath.read_video")  and request.user.has_perm("askmath.access_manager"):
            lesson, video = None, None
            try:
                lesson = ContactModel.objects.get(id = id_lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return self.choose_lesson(request)
            try:
                video = VideoModel.objects.get(id = id_video)
            except Exception, e:
                print e
                messages.error(request, TextMessage.VIDEO_NOT_FOUND)
                return self.view_videos(request, id_lesson)
            try:
                if lesson != None and video != None:
                    return self.__video.view_video(request, lesson, video)
                else:
                    messages.error(request, TextMessage.ERROR)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_videos(request, id_lesson)
    
    @method_decorator(login_required)
    def add_video(self, request, id_lesson):
        if request.user.has_perm("askmath.write_video")  and request.user.has_perm("askmath.access_manager"):
            try:
                lesson = ContactModel.objects.get(id = id_lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return self.choose_lesson(request)
            try:
                return self.__video.add_video(request, lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.VIDEO_ERROR_ADD)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_videos(request, id_lesson)
    
    @method_decorator(login_required)
    def remove_video(self, request, id_lesson, id_video):
        if request.user.has_perm("askmath.write_video")  and request.user.has_perm("askmath.access_manager"):
            try:
                lesson = ContactModel.objects.get(id = id_lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return self.choose_lesson(request )
            try:
                video = VideoModel.objects.get(id = id_video)
            except Exception, e:
                print e
                messages.error(request, TextMessage.VIDEO_NOT_FOUND)
                return self.view_videos(request, id_lesson)
            try:    
                return self.__video.remove_video(request, lesson,video)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_videos(request, id_lesson)
    
    @method_decorator(login_required)
    def edit_video(self, request, id_lesson, id_video):
        if request.user.has_perm("askmath.write_video")  and request.user.has_perm("askmath.access_manager"):
            try:
                lesson = ContactModel.objects.get(id = id_lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return self.choose_lesson(request )
            try:
                video = VideoModel.objects.get(id = id_video)
            except Exception, e:
                print e
                messages.error(request, TextMessage.VIDEO_NOT_FOUND)
                return self.view_videos(request, id_lesson)
            try:
                return self.__video.edit_video(request, lesson, video)
            except Exception, e:
                print e
                messages.error(request, TextMessage.VIDEO_ERROR_EDIT)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_videos(request, id_lesson)

    @method_decorator(login_required)
    def restore_video(self, request, id_lesson,id_video):
        if request.user.has_perm("askmath.write_video")  and request.user.has_perm("askmath.access_manager"):
            try:
                lesson = ContactModel.objects.get(id = id_lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return self.choose_lesson(request )
            try:
                video = VideoModel.objects.get(id = id_video)
            except Exception, e:
                print e
                messages.error(request, TextMessage.VIDEO_NOT_FOUND)
                return self.view_videos(request, id_lesson)
            try:
                return self.__video.restore_video(request, lesson,video)
            except Exception, e:
                print e
                messages.error(request, TextMessage.VIDEO_ERROR_RESTORE)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_videos(request, id_lesson)
            
    @method_decorator(login_required)
    def sort_videos(self, request, id_lesson):
        if request.user.has_perm("askmath.read_video")  and request.user.has_perm("askmath.access_manager"):
            try:
                lesson = ContactModel.objects.get(id = id_lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return self.choose_lesson(request )
            try:
                if lesson:
                    if request.method == "POST":
                        new_order = json.loads(request.POST['new_order'])
                        return self.__video.sort_videos(request,lesson,new_order)
                    else:
                        return self.__video.sort_videos(request,lesson,None)
            except Exception, e:
                print e
                messages.error(request, TextMessage.VIDEO_ERROR_SORT)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_videos(request, id_lesson)