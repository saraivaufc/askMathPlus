from .discipline import Discipline
from .idiscipline import IDiscipline


class ProxyDiscipline(IDiscipline):
    def __init__(self):
        self.__discipline = Discipline()
    def get(self, request):
        return self.__discipline.get(request)
        