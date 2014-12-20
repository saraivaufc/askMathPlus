from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
import md5

def register(request):
	try:
		user = User.objects.create(
			username = request.POST['username'],
			email = request.POST['email'],
			first_name = request.POST['first_name'],
			last_name = request.POST['last_name'],
			password = md5.new( request.POST['password'] ).hexdigest(),
		)
		user.save()
		return render(request , 'cadastro/criarContaSucesso.php', locals())
	except:
		return render(request , 'cadastro/criarContaFalha.php', locals())