from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.models.lesson import Lesson as ContactModel
from askmath.models.video import Video as VideoModel
from askmath.entities import Message, TextMessage, TypeMessage
from askmath.views.index import Home

from .ivideo import IVideo
from .video import Video
import json

class ProxyVideo(IVideo):
    
    def __init__(self):
        self.__video = Video()
        self.__home = Home()
    
    def choose_lesson(self, request, message = None):
        if request.user.has_perm("askmath.read_video"):
            try:
                return self.__video.choose_lesson(request, message)
            except:
                message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.__home.index(request, message)
    
    def view_videos(self, request, id_lesson, message = None):
        if request.user.has_perm("askmath.read_video"):
            try:
                lesson = ContactModel.objects.get(id = id_lesson)
            except:
                message = Message(TextMessage.LESSON_NOT_FOUND, TypeMessage.ERROR)
                return self.choose_lesson(request , message)
            try:
                if lesson:
                    return self.__video.view_videos(request,lesson,  message)
            except:
                message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.choose_lesson(request , message)
    
    def view_videos_removed(self, request, id_lesson,  message = None):
        if request.user.has_perm("askmath.read_video"):
            try:
                lesson = ContactModel.objects.get(id = id_lesson)
            except:
                message = Message(TextMessage.LESSON_NOT_FOUND, TypeMessage.ERROR)
                return self.choose_lesson(request , message)
            try:
                if lesson:
                    return self.__video.view_videos_removed(request,lesson,  message)
            except:
                message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.choose_lesson(request , message)
    
    def view_video(self, request, id_lesson, id_video, message=None):
        if request.user.has_perm("askmath.read_video"):
            lesson, video = None, None
            try:
                lesson = ContactModel.objects.get(id = id_lesson)
            except:
                message = Message(TextMessage.LESSON_NOT_FOUND, TypeMessage.ERROR)
                return self.choose_lesson(request , message)
            try:
                video = VideoModel.objects.get(id = id_video)
            except:
                message = Message(TextMessage.VIDEO_NOT_FOUND, TypeMessage.ERROR)
                return self.view_videos(request, id_lesson, message)
            #try:
            if lesson != None and video != None:
                return self.__video.view_video(request, lesson, video)
            else:
                message = Message(TextMessage.ERROR,TypeMessage.ERROR)
            #except:
                #message = Message(TextMessage.ERROR,TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION,TypeMessage.ERROR)
        return self.view_videos(request, id_lesson, message)
    
    def add_video(self, request, id_lesson, message=None):
        if request.user.has_perm("askmath.write_video"):
            try:
                lesson = ContactModel.objects.get(id = id_lesson)
            except:
                message = Message(TextMessage.LESSON_NOT_FOUND, TypeMessage.ERROR)
                return self.choose_lesson(request , message)
            try:
                return self.__video.add_video(request, lesson)
            except:
                message = Message(TextMessage.VIDEO_ERROR_ADD, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION,TypeMessage.ERROR)
        return self.view_videos(request, id_lesson, message)
    
    def remove_video(self, request, id_lesson, id_video):
        if request.user.has_perm("askmath.write_video"):
            try:
                lesson = ContactModel.objects.get(id = id_lesson)
            except:
                message = Message(TextMessage.LESSON_NOT_FOUND, TypeMessage.ERROR)
                return self.choose_lesson(request , message)
            try:
                video = VideoModel.objects.get(id = id_video)
            except:
                message = Message(TextMessage.VIDEO_NOT_FOUND, TypeMessage.ERROR)
                return self.view_videos(request, id_lesson, message)
            try:    
                return self.__video.remove_video(request, lesson,video)
            except:
                message = Message(TextMessage.ERROR,TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION,TypeMessage.ERROR)
        return self.view_videos(request, id_lesson, message)
    
    def edit_video(self, request, id_lesson, id_video, message=None):
        if request.user.has_perm("askmath.write_video"):
            try:
                lesson = ContactModel.objects.get(id = id_lesson)
            except:
                message = Message(TextMessage.LESSON_NOT_FOUND, TypeMessage.ERROR)
                return self.choose_lesson(request , message)
            try:
                video = VideoModel.objects.get(id = id_video)
            except:
                message = Message(TextMessage.VIDEO_NOT_FOUND, TypeMessage.ERROR)
                return self.view_videos(request, id_lesson, message)
            try:
                return self.__video.edit_video(request, lesson, video)
            except:
                message = Message(TextMessage.VIDEO_ERROR_EDIT,TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION,TypeMessage.ERROR)
        return self.view_videos(request, id_lesson, message)

    
    def restore_video(self, request, id_lesson,id_video):
        if request.user.has_perm("askmath.write_video"):
            try:
                lesson = ContactModel.objects.get(id = id_lesson)
            except:
                message = Message(TextMessage.LESSON_NOT_FOUND, TypeMessage.ERROR)
                return self.choose_lesson(request , message)
            try:
                video = VideoModel.objects.get(id = id_video)
            except:
                message = Message(TextMessage.VIDEO_NOT_FOUND, TypeMessage.ERROR)
                return self.view_videos(request, id_lesson, message)
            try:
                return self.__video.restore_video(request, lesson,video)
            except:
                message = Message(TextMessage.VIDEO_ERROR_RESTORE,TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION,TypeMessage.ERROR)
        return self.view_videos(request, id_lesson, message)
            
    def sort_videos(self, request, id_lesson, message = None):
        if request.user.has_perm("askmath.read_video"):
            try:
                lesson = ContactModel.objects.get(id = id_lesson)
            except:
                message = Message(TextMessage.LESSON_NOT_FOUND, TypeMessage.ERROR)
                return self.choose_lesson(request , message)
            try:
                if lesson:
                    if request.method == "POST":
                        new_order = json.loads(request.POST['new_order'])
                        return self.__video.sort_videos(request,lesson,new_order, message)
                    else:
                        return self.__video.sort_videos(request,lesson,None, message)
            except:
                message = Message(TextMessage.VIDEO_ERROR_SORT, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION,TypeMessage.ERROR)
        return self.view_videos(request, id_lesson, message)