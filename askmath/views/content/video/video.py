from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.entities import Message, TextMessage, TypeMessage


from askMathPlus.settings import COLORS_ALL
from django.utils.translation import ugettext_lazy as _

from .ivideo import IVideo

class Video(IVideo):
    def view_videos(self, request, discipline, lesson, message=None):
        videos = lesson.get_videos()
        return render(request, "askmath/content/video/view_videos.html",
            {'request': request, 'discipline': discipline, 'lesson': lesson,'videos': videos,'colors': COLORS_ALL, 'message': message})
    
    def view_video(self, request, discipline, lesson,video,  message=None):
        return render(request, "askmath/content/video/view_video.html",
            {'request': request, 'discipline': discipline, 'lesson': lesson,'video': video,'colors': COLORS_ALL,'message': message})