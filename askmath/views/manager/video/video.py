from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.utils.translation import ugettext_lazy as _
from askmath.entities import TextMessage
from django.contrib import messages
from askmath.forms import VideoForm, ItemForm
from askmath.models.discipline import Discipline as CategoryModel
from askmath.models.lesson import Lesson as ContactModel
from askmath.models.video import Video as VideoModel

from .ivideo import IVideo


class Video(IVideo):
    def choose_lesson(self, request):
        disciplines = []
        for discipline in CategoryModel.objects.filter(exists=True):
            if discipline.get_lessons():
                disciplines.append(discipline) 
        return render(request, "askmath/manager/video/manager_choose_lessons.html",
            {'request':request,'disciplines': disciplines})
    
    def view_videos(self, request, lesson):
        videos = lesson.get_videos()
        return render(request, "askmath/manager/video/manager_view_videos.html",
            {'request':request,'videos': videos, 'lesson': lesson})
    
    def view_videos_removed(self, request, lesson):
        videos = VideoModel.objects.filter(exists=False,lesson = lesson.id)
        return render(request, "askmath/manager/video/manager_view_videos.html",
            {'request':request,'videos': videos, 'lesson': lesson,'is_removed': True })
    
    def view_video(self, request, lesson, video):
        return render(request, "askmath/manager/video/manager_view_video.html", 
            {'request':request,'lesson': lesson,'video': video })
    
    
    
    def add_video(self, request, lesson):
        if request.method == "POST":
            request.POST = request.POST.copy()
            request.POST['lesson'] = lesson.id
            try:
                positions = map(lambda x: x.position, lesson.get_videos())
            except Exception, e:
                print e
                positions = [0,]
            if not positions or len(positions):
                positions = [0,]
            request.POST['position']= max(positions)+1
            form = VideoForm(request.POST, request.FILES)
            if form.is_valid():
                video = form.save()
                messages.success(request, TextMessage.VIDEO_SUCCESS_ADD)
                return self.view_video(request, lesson, video)
            else:
                messages.error(request, TextMessage.ERROR_FORM)
        else:
            form = VideoForm()
        return render(request, "askmath/manager/video/manager_form_video.html", 
            {'request':request,'form': form,'lesson': lesson, 'title_form':_('Create Video')})
    
    def remove_video(self, request, lesson, video):
        video.delete()
        messages.success(request, TextMessage.VIDEO_SUCCESS_REM)
        return self.view_videos(request, lesson)
    
    def edit_video(self, request, lesson, video):
        if request.method == "POST":
            request.POST = request.POST.copy()
            request.POST['lesson'] = lesson.id
            
            form = VideoForm(request.POST, request.FILES, instance=video)
            if form.is_valid():
                video = form.save()
                messages.success(request, TextMessage.VIDEO_SUCCESS_EDIT)
                return self.view_video(request, lesson, video)
            else:
                messages.error(request, TextMessage.ERROR_FORM)
        else:
            form = VideoForm(instance=video)
        return render(request, "askmath/manager/video/manager_form_video.html", 
            {'request':request,'form': form, 'lesson': lesson,'video':video, 'title_form':_('Edit Video')})
    
    
    def restore_video(self, request, lesson, video):
        video.restore()
        messages.success(request, TextMessage.VIDEO_SUCCESS_RESTORE)
        return self.view_videos(request, lesson)
    
    def sort_videos(self, request, lesson,new_order=None):
        videos = VideoModel.objects.filter(exists=True, visible=True,lesson = lesson.id)
        if request.method == 'POST':    
            try:
                for index, i in enumerate(new_order):
                    VideoModel.objects.filter(id = i).update(position = index + 1)
                    messages.success(request, VIDEO_SUCCESS_SORT)
                request.method = "GET"
                return self.sort_videos(request, lesson, None)
            except Exception, e:
                print e
                messages.error(request, TextMessage.VIDEO_ERROR_SORT)
        return render(request, "askmath/manager/video/manager_view_videos_sort.html",
            {'request':request,'videos': videos, 'lesson': lesson})
    