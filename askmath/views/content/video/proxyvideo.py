from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from askmath.entities import Message, TextMessage, TypeMessage

#MODELS
from askmath.models.discipline import Discipline as DisciplineModel
from askmath.models.lesson import Lesson as LessonModel
from askmath.models.video import Video as VideoModel

from askmath.views.initial import Home



from .ivideo import IVideo
from .video import Video


class ProxyVideo(IVideo):
    def __init__(self):
        self.__video = Video()
        self.__home = Home()
        
    def view_videos(self, request, id_discipline, id_lesson, message=None):
        if request.user.has_perm("askmath.read_video"):
            try:
                discipline = DisciplineModel.objects.filter(id = id_discipline, exists=True,visible=True)[0]
            except:
                message = Message(TextMessage.DISCIPLINE_NOT_FOUND, TypeMessage.ERROR)
                return self.__home.index(request, message)
            try:
                lesson = LessonModel.objects.filter(id = id_lesson, exists=True,visible=True)[0]
            except:
                message = Message(TextMessage.LESSON_NOT_FOUND, TypeMessage.ERROR)
                return self.__home.index(request, message)
            #try:
            return self.__video.view_videos(request, discipline, lesson, message)
            #except:
                #message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.__home.index(request, message)
    
    def view_video(self, request, id_discipline, id_lesson, id_video, message=None):
        if request.user.has_perm("askmath.read_video"):
            try:
                discipline = DisciplineModel.objects.filter(id = id_discipline, exists=True,visible=True)[0]
            except:
                message = Message(TextMessage.DISCIPLINE_NOT_FOUND, TypeMessage.ERROR)
                return self.view_videos(request, id_discipline, id_lesson, message)
            try:
                lesson = LessonModel.objects.filter(id = id_lesson, exists=True,visible=True)[0]
            except:
                message = Message(TextMessage.LESSON_NOT_FOUND, TypeMessage.ERROR)
                return self.view_videos(request, id_discipline, id_lesson, message)
            try:
                video = VideoModel.objects.filter(id = id_video, exists=True,visible=True)[0]
            except:
                message = Message(TextMessage.VIDEO_NOT_FOUND, TypeMessage.ERROR)
                return self.view_videos(request, id_discipline, id_lesson, message)
            if not video in lesson.get_videos():
                message = Message(TextMessage.VIDEO_NOT_FOUND_IN_LESSON, TypeMessage.ERROR)
                return self.view_videos(request, id_discipline, id_lesson, message)

            #try:
            return self.__video.view_video(request, discipline, lesson, video)
            #except:
                #message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.__home.index(request, message)