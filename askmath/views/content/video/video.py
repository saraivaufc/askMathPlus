from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.translation import ugettext_lazy as _

from .ivideo import IVideo

class Video(IVideo):
    def view_videos(self, request, discipline, lesson):
        videos = lesson.get_videos_visibles()
        return render(request, "askmath/content/video/view_videos.html",
            {'request': request, 'discipline': discipline, 'lesson': lesson,'videos': videos})
    
    def view_video(self, request, discipline, lesson,video):
        return render(request, "askmath/content/video/view_video.html",
            {'request': request, 'discipline': discipline, 'lesson': lesson,'video': video})