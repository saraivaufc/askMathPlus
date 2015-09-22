from .idiscipline import IDiscipline
from .discipline import Discipline
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from askmath.entities import Message, TextMessage, TypeMessage
from ..lesson import ProxyLesson

from askmath.models.discipline import Discipline as DisciplineModel
from askmath.models.lesson import Lesson as LessonModel


class ProxyDiscipline(IDiscipline):
    def __init__(self):
    	self.__discipline = Discipline()
    	self.__proxylesson = ProxyLesson()

    @method_decorator(login_required)
    def view_discipline(self, request, id_discipline, message=None):
    	if request.user.has_perm("askmath.read_discipline")  and request.user.has_perm("askmath.access_content"):
            try:
                discipline = DisciplineModel.objects.get(id = id_discipline,exists=True)
            except:
                message = Message(TextMessage.DISCIPLINE_NOT_FOUND, TypeMessage.ERROR)
                return self.__proxylesson.view_lessons(request,message)
            
            try:
                return self.__discipline.view_discipline(request,discipline, message)
            except Exception, e:
            	print e
            	message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.__proxylesson.view_lessons(request,message)