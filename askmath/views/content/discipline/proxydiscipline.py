from .idiscipline import IDiscipline
from .discipline import Discipline
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from askmath.entities import TextMessage
from django.contrib import messages
from ..lesson import ProxyLesson

from askmath.models.discipline import Discipline as DisciplineModel
from askmath.models.lesson import Lesson as LessonModel


class ProxyDiscipline(IDiscipline):
    def __init__(self):
    	self.__discipline = Discipline()
    	self.__proxylesson = ProxyLesson()

    @method_decorator(login_required)
    def view_discipline(self, request, id_discipline):
    	if request.user.has_perm("askmath.read_discipline")  and request.user.has_perm("askmath.access_content"):
            try:
                discipline = DisciplineModel.objects.get(id = id_discipline,exists=True)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return self.__proxylesson.view_lessons(request)
            
            try:
                return self.__discipline.view_discipline(request,discipline)
            except Exception, e:
            	print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.__proxylesson.view_lessons(request)