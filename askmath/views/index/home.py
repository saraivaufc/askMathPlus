# -*- coding: UTF-8 -*-

from askmath.entities import TextMessage
from django.utils.translation import ugettext as _
from django.core.mail import EmailMultiAlternatives
from askmath.forms import MessageForm, MessageFormRecaptcha
from askmath.models import Discipline as DisciplineModel
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.template import loader, Context
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .ihome import IHome
from askMathPlus.settings import EMAIL_ADMINS, BASE_DIR
from django.conf import settings


class Home(IHome):
	def index(self, request):
		if request.user.is_authenticated():
			if request.user.has_perm('askmath.access_manager'):
				return HttpResponseRedirect(reverse('askmath:manager_view'))
			elif request.user.has_perm('askmath.access_content'):
				return HttpResponseRedirect(reverse('askmath:content_view'))

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
				message = form.save()
				messages.success(request, TextMessage.MESSAGE_SUCCESS_SEND)
				t = loader.get_template('askmath/index/contact_email.html')
				c = Context({ 'message': message, 'SITE_URL': settings.SITE_URL})
				rendered = t.render(c)
				msg = EmailMultiAlternatives(_("AskMath - Contact"), rendered,  message.get_email(), EMAIL_ADMINS,)
				msg.attach_alternative(rendered , "text/html")
				msg.send()
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
