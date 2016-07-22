from .ilesson import ILesson
from .lesson import Lesson


class ProxyLesson(ILesson):
    def __init__(self):
        self.__contact = Lesson()

    def get(self, request):
        return self.__contact.get(request)
