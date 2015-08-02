from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.utils.translation import ugettext_lazy as _

from askMathPlus.settings import COLORS_ALL
from askmath.entities import Message, TextMessage, TypeMessage
from askmath.forms import VideoForm, ItemForm
from askmath.models.discipline import Discipline as DisciplineModel
from askmath.models.lesson import Lesson as LessonModel
from askmath.models.video import Video as VideoModel

from .ivideo import IVideo


class Video(IVideo):
    def choose_lesson(self, request, message = None):
        disciplines = []
        for discipline in DisciplineModel.objects.filter(exists=True):
            if discipline.get_lessons():
                disciplines.append(discipline) 
        return render(request, "askmath/manager/video/manager_choose_lessons.html",
            {'request':request,'disciplines': disciplines, 'colors': COLORS_ALL, 'message': message})
    
    def view_videos(self, request, lesson, message = None):
        videos = lesson.get_videos()
        return render(request, "askmath/manager/video/manager_view_videos.html",
            {'request':request,'videos': videos, 'lesson': lesson, 'colors': COLORS_ALL, 'message': message})
    
    def view_videos_removed(self, request, lesson, message = None):
        videos = VideoModel.objects.filter(exists=False,lesson = lesson.id)
        return render(request, "askmath/manager/video/manager_view_videos.html",
            {'request':request,'videos': videos, 'lesson': lesson,'is_removed': True ,'colors': COLORS_ALL, 'message': message})
    
    def view_video(self, request, lesson, video, message = None):
        return render(request, "askmath/manager/video/manager_view_video.html", 
            {'request':request,'lesson': lesson,'video': video , 'message': message, 'colors': COLORS_ALL })
    
    
    
    def add_video(self, request, lesson, message = None):
        if request.method == "POST":
            request.POST = request.POST.copy()
            request.POST['lesson'] = lesson.id
            
            try:
                positions = map(lambda x: x.position, lesson.get_videos())
            except:
                positions = [0]
            if not positions:
                positions = [0]
                
            request.POST['position']= max(positions)+1
            form = VideoForm(request.POST, request.FILES)
            if form.is_valid():
                video = form.save()
                message = Message(TextMessage.VIDEO_SUCCESS_ADD, TypeMessage.SUCCESS)
                return self.view_video(request, lesson, video, message)
        else:
            form = VideoForm()
        return render(request, "askmath/manager/video/manager_form_video.html", 
            {'request':request,'form': form,'lesson': lesson, 'title_form':_('Create Video'), 'message': message})
    
    def remove_video(self, request, lesson, video, message = None):
        video.delete()
        message = Message(TextMessage.VIDEO_SUCCESS_REM, TypeMessage.SUCCESS)
        return self.view_videos(request, lesson, message)
    
    def edit_video(self, request, lesson, video,  message = None):
        if request.method == "POST":
            request.POST = request.POST.copy()
            request.POST['video-lesson'] = lesson.id
            
            form = VideoForm(request.POST, request.FILES, instance=video)
            if form.is_valid():
                video = form.save()
                message = Message(TextMessage.VIDEO_SUCCESS_EDIT, TypeMessage.SUCCESS)
                return self.view_video(request, lesson, video, message)
        else:
            form = VideoForm(instance=video)
        return render(request, "askmath/manager/video/manager_form_video.html", 
            {'request':request,'form': form, 'lesson': lesson, 'title_form':_('Edit Video'), 'message': message})
    
    
    def restore_video(self, request, lesson, video):
        video.restore()
        message = Message(TextMessage.VIDEO_SUCCESS_RESTORE, TypeMessage.SUCCESS)
        return self.view_videos(request, lesson, message)
    
    def sort_videos(self, request, lesson,new_order=None, message=None):
        videos = VideoModel.objects.filter(exists=True, visible=True,lesson = lesson.id)
        if request.method == 'POST':    
            try:
                for index, i in enumerate(new_order):
                    VideoModel.objects.filter(id = i).update(position = index + 1)
                message = Message(TextMessage.VIDEO_SUCCESS_SORT, TypeMessage.SUCCESS)
                request.method = "GET"
                return self.sort_videos(request, lesson, None, message)
            except:
                message = Message(TextMessage.VIDEO_ERROR_SORT, TypeMessage.ERROR)
        return render(request, "askmath/manager/video/manager_view_videos_sort.html",
            {'request':request,'videos': videos, 'lesson': lesson, 'colors': COLORS_ALL, 'message': message})
    