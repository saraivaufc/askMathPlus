import json
from askmath.entities import TextMessage
from askmath.models.discipline import Discipline as DisciplineModel
from askmath.models.lesson import Lesson as LessonModel
from askmath.models.video import Video as VideoModel
from askmath.views.index import ProxyHome
from askmath.views.manager.lesson import ProxyLesson
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .ivideo import IVideo
from .video import Video


class ProxyVideo(IVideo):
    
    def __init__(self):
        self.__video = Video()
        self.__proxy_home = ProxyHome()
        self.__proxy_lesson = ProxyLesson()
    
    @method_decorator(login_required)
    def view_videos(self, request, id_lesson, id_discipline):
        if request.user.has_perm("askmath.read_video")  and request.user.has_perm("askmath.access_manager"):
            try:
                lesson = LessonModel.objects.get(id = id_lesson)
            except Exception, e:
                print e
                messages.error(request,TextMessage.LESSON_NOT_FOUND)
                return self.__proxy_lesson.view_lessons(request, id_discipline)
            try:
                discipline = DisciplineModel.objects.get(id = id_discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return self.__proxy_lesson.view_lessons(request, id_discipline)
            
            try:
                return self.__video.view_videos(request,lesson, discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.__proxy_lesson.view_lessons(request, id_discipline)
    
    @method_decorator(login_required)
    def view_videos_removed(self, request, id_lesson, id_discipline):
        if request.user.has_perm("askmath.read_video")  and request.user.has_perm("askmath.access_manager"):
            try:
                lesson = LessonModel.objects.get(id = id_lesson)
            except Exception, e:
                print e
                messages.error(request,TextMessage.LESSON_NOT_FOUND)
                return self.view_videos(request, id_lesson, id_discipline)
            try:
                discipline = DisciplineModel.objects.get(id = id_discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return self.view_videos(request, id_lesson, id_discipline)
            
            try:
                return self.__video.view_videos_removed(request,lesson, discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_videos(request, id_lesson, id_discipline)
    
    @method_decorator(login_required)
    def add_video(self, request, id_lesson, id_discipline):
        if request.user.has_perm("askmath.write_video")  and request.user.has_perm("askmath.access_manager"):
            try:
                lesson = LessonModel.objects.get(id = id_lesson)
            except Exception, e:
                print e
                messages.error(request,TextMessage.LESSON_NOT_FOUND)
                return self.view_videos(request, id_lesson, id_discipline)
            try:
                discipline = DisciplineModel.objects.get(id = id_discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return self.view_videos(request, id_lesson, id_discipline)
            
            try:
                return self.__video.add_video(request, lesson, discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.VIDEO_ERROR_ADD)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_videos(request, id_lesson, id_discipline)
    
    @method_decorator(login_required)
    def remove_video(self, request, id_video, id_lesson, id_discipline):
        if request.user.has_perm("askmath.write_video")  and request.user.has_perm("askmath.access_manager"):
            try:
                video = VideoModel.objects.get(id = id_video)
            except Exception, e:
                print e
                messages.error(request, TextMessage.VIDEO_NOT_FOUND)
                return self.view_videos(request, id_lesson, id_discipline)
            try:
                lesson = LessonModel.objects.get(id = id_lesson)
            except Exception, e:
                print e
                messages.error(request,TextMessage.LESSON_NOT_FOUND)
                return self.view_videos(request, id_lesson, id_discipline)
            try:
                discipline = DisciplineModel.objects.get(id = id_discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return self.view_videos(request, id_lesson, id_discipline)
            
            try:    
                return self.__video.remove_video(request,video, lesson, discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_videos(request, id_lesson, id_discipline)
    
    @method_decorator(login_required)
    def edit_video(self, request, id_video ,id_lesson, id_discipline):
        if request.user.has_perm("askmath.write_video")  and request.user.has_perm("askmath.access_manager"):
            try:
                video = VideoModel.objects.get(id = id_video)
            except Exception, e:
                print e
                messages.error(request, TextMessage.VIDEO_NOT_FOUND)
                return self.view_videos(request, id_lesson, id_discipline)
            try:
                lesson = LessonModel.objects.get(id = id_lesson)
            except Exception, e:
                print e
                messages.error(request,TextMessage.LESSON_NOT_FOUND)
                return self.view_videos(request, id_lesson, id_discipline)
            try:
                discipline = DisciplineModel.objects.get(id = id_discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return self.view_videos(request, id_lesson, id_discipline)
            
            try:
                return self.__video.edit_video(request, video, lesson, discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.VIDEO_ERROR_EDIT)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_videos(request, id_lesson, id_discipline)

    @method_decorator(login_required)
    def restore_video(self, request,id_video, id_lesson,id_discipline):
        if request.user.has_perm("askmath.write_video")  and request.user.has_perm("askmath.access_manager"):
            try:
                video = VideoModel.objects.get(id = id_video)
            except Exception, e:
                print e
                messages.error(request, TextMessage.VIDEO_NOT_FOUND)
                return self.view_videos(request, id_lesson, id_discipline)
            try:
                lesson = LessonModel.objects.get(id = id_lesson)
            except Exception, e:
                print e
                messages.error(request,TextMessage.LESSON_NOT_FOUND)
                return self.view_videos(request, id_lesson, id_discipline)
            try:
                discipline = DisciplineModel.objects.get(id = id_discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return self.view_videos(request, id_lesson, id_discipline)
            try:
                return self.__video.restore_video(request, video, lesson, discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.VIDEO_ERROR_RESTORE)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_videos(request, id_lesson, id_discipline)
            
    @method_decorator(login_required)
    def sort_videos(self, request, id_lesson, id_discipline):
        if request.user.has_perm("askmath.read_video")  and request.user.has_perm("askmath.access_manager"):
            try:
                lesson = LessonModel.objects.get(id = id_lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return self.view_videos(request, id_lesson, id_discipline)
            try:
                discipline = DisciplineModel.objects.get(id = id_discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return self.view_videos(request, id_lesson, id_discipline)
            try:
                if request.method == "POST":
                    new_order = json.loads(request.POST['new_order'])
                    return self.__video.sort_videos(request,lesson, discipline, new_order)
                else:
                    return self.__video.sort_videos(request,lesson, discipline, None)
            except Exception, e:
                print e
                messages.error(request, TextMessage.VIDEO_ERROR_SORT)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_videos(request, id_lesson, id_discipline)