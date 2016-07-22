# -*- coding: UTF-8 -*-

from askmath.entities import TextMessage
from askmath.forms import MessageForm, MessageFormRecaptcha
from askmath.models import Discipline as DisciplineModel
from django.contrib import messages
from django.shortcuts import render
from .ihome import IHome


class Home(IHome):
    def index(self, request):
        if request.user.is_authenticated():
            if request.user.has_perm('askmath.access_manager'):
                disciplines = DisciplineModel.objects.filter(exists=True, visible=True)
                return render(request, 'askmath/manager/manager_home.html',
                              {'request': request, 'disciplines': disciplines})
            elif request.user.has_perm('askmath.access_content'):
                from askmath.views.content.discipline import ProxyDiscipline as ProxyDisciplineContent
                proxy_discipline_content = ProxyDisciplineContent()
                return proxy_discipline_content.view_disciplines(request)

        return render(request, 'askmath/index/home.html', {'request': request})

    def about(self, request):
        return render(request, 'askmath/index/about.html',
                      {'request': request})

    def message(self, request):

        if request.method == "POST":
            if request.user.is_authenticated():
                form = MessageForm(request.POST, request.FILES)
            else:
                form = MessageFormRecaptcha(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, TextMessage.MESSAGE_SUCCESS_SEND)
                return self.index(request)
            else:
                messages.error(request, TextMessage.ERROR_FORM)
        else:
            if request.user.is_authenticated():
                form = MessageForm()
            else:
                form = MessageFormRecaptcha()
        return render(request, 'askmath/index/message.html',
                      {'request': request, 'form': form})

    def terms(self, request):
        return render(request, 'askmath/index/terms.html',
                      {'request': request})

    def policies(self, request):
        return render(request, 'askmath/index/policies.html',
                      {'request': request})

    def credits(self, request):
        return render(request, 'askmath/index/credits.html',
                      {'request': request})

    def contents(self, request, lesson=None):
        if lesson:
            return render(request, 'askmath/index/contents_details.html',
                          {'request': request, 'lesson': lesson})
        else:
            disciplines = DisciplineModel.objects.filter(exists=True, visible=True)
            return render(request, 'askmath/index/contents.html',
                          {'request': request, 'disciplines': disciplines})
