from askmath.entities import TextMessage
from askmath.forms import StudentForm, AssistantForm, TeacherForm, AdministratorForm, RegisterForm
from askmath.forms.users import LoginForm, RecoverPassword
from askmath.models.access import AdministratorKey, TeacherKey, AssistantKey
from django.contrib import messages
from django.contrib.auth import authenticate, login as login_user
from django.contrib.auth import logout as auth_logout
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .iaccount import IAccount

try:
	from hashlib import md5
except:
	from md5 import new as md5


class Account(IAccount):
	def options(self, request):
		form_signin = None
		form_signup = None
		form_recover_password = None
		tab_actived = None

		if request.method == 'POST':
			try:
				option = request.POST['option']
				if option == 'sign_in':
					form_signin = LoginForm(request.POST)
					tab_actived = 'sign_in'
				elif option == 'sign_up':
					form_signup = RegisterForm(request.POST)
					tab_actived = 'sign_up'
				elif option == 'recover_password':
					form_recover_password = RecoverPassword(request.POST)
					tab_actived = 'recover_password'
			except Exception, e:
				print e
		if not form_signin:
			form_signin = LoginForm()
		if not form_signup:
			form_signup = RegisterForm()
		if not form_recover_password:
			form_recover_password = RecoverPassword()

		return render(request, "askmath/authentication/options.html",
					  {'request': request,
					   'form_signin': form_signin,
					   'form_signup': form_signup,
					   'tab_actived': tab_actived})

	def signin(self, request, form=None):
		next = None
		try:
			if request.method == 'GET':
				next = request.GET['next']
			elif request.method == 'POST':
				next = request.POST['next']
		except Exception, e:
			print e

		if request.method == 'POST':
			form = LoginForm(request.POST)
			if form.is_valid():
				user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
				try:
					login_user(request, user)
					if next:
						return HttpResponseRedirect(next)
					else:
						return HttpResponseRedirect(reverse('askmath:home'))
				except Exception, e:
					messages.error(request, TextMessage.USERNAME_OR_PASSWORD_INCORRECT)
			else:
				messages.error(request, TextMessage.ERROR_FORM)
		return HttpResponseRedirect(reverse('askmath:authentication_options'))

	def signup(self, request):
		request.POST = request.POST.copy()

		group_name = request.POST['group']
		form = None
		register_key = None

		if group_name == "student":
			form = StudentForm(request.POST, request.FILES)
		else:
			key = request.POST['key']
			if group_name == "assistant":
				try:
					register_key = AssistantKey.objects.get(key=key, exists=True, in_use=False)
					form = AssistantForm(request.POST, request.FILES)
				except Exception, e:
					print e
					messages.error(request, TextMessage.KEY_NOT_FOUND)
					return HttpResponseRedirect(reverse('askmath:authentication_options'))
			elif group_name == "teacher":
				try:
					register_key = TeacherKey.objects.get(key=key, exists=True, in_use=False)
					form = TeacherForm(request.POST, request.FILES)
				except Exception, e:
					print e
					messages.error(request, TextMessage.KEY_NOT_FOUND)
					return HttpResponseRedirect(reverse('askmath:authentication_options'))
			elif group_name == "administrator":
				try:
					register_key = AdministratorKey.objects.get(key=key, exists=True, in_use=False)
					form = AdministratorForm(request.POST, request.FILES)
				except Exception, e:
					print e
					messages.error(request, TextMessage.KEY_NOT_FOUND)
					return HttpResponseRedirect(reverse('askmath:authentication_options'))
			else:
				print "group name", group_name
				messages.error(request, TextMessage.USER_GROUP_NOT_FOUND)
				return HttpResponseRedirect(reverse('askmath:authentication_options'))
		if form and form.is_valid():
			user = form.save(commit=False)
			user.set_password(user.password)
			user.save(group=group_name)
			if register_key:
				register_key.add_user(user)
			messages.success(request, TextMessage.USER_CREATED_SUCCESS)
		return self.signin(request)

	def logout(self, request):
		try:
			auth_logout(request)
		except Exception, e:
			print e
		return HttpResponseRedirect(reverse('askmath:authentication_options'))
