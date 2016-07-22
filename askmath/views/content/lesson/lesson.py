from django.shortcuts import render
from .ilesson import ILesson


class Lesson(ILesson):
    def view_lesson(self, request, discipline, lesson):
        return render(request, "askmath/content/lesson/content_view_lesson.html",
                      {'request': request, 'discipline': discipline, 'lesson': lesson})
