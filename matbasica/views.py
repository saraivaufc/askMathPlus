# -*- encoding=utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from matbasica.models import *
from django.core.mail import send_mail
import md5
import re
from random import randrange
import smtplib
from email.mime.text import MIMEText
from django.contrib.auth.views import login as login_view
from spirit.forms.user import LoginForm
from django.contrib.auth.views import logout as logout_sys
from spirit.utils.ratelimit.decorators import ratelimit
from django.test import Client

def index(request):
	if "usuario" in request.session:
		return HttpResponseRedirect('/principal/')
	else:
		return HttpResponseRedirect('/login/')

def login(request, **kwargs):
	if request.user.is_authenticated() and request.user.is_moderator == False:
		return HttpResponseRedirect('/principal/')

	if request.method == "POST":
		c = Client()
		c.login(username = 'id_username', password = 'id_password')
	
	return login_view(request, authentication_form=LoginForm, **kwargs)


def login_falha(request):
	return render(request , 'login/login_falha.php' , locals())

def logout(request):
	logout_sys(request)
	return HttpResponseRedirect('/login/')

def criarConta(request):
	if request.method == 'POST':
		try:
			user = Usuario.objects.create(
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
	return render(request , 'cadastro/criarConta.php' , locals())

def principal(request):
	if request.user.is_authenticated():
		try:
			usuario = Usuario.objects.get(username = request.user)
		except:
			return HttpResponseRedirect('/login/falha')

		if request.method == 'POST':
			Usuario.objects.filter(id = usuario.id).update(turma = request.POST['opcao'])
			return HttpResponseRedirect('/principal/')
		else:
			try:
				turma = Turma.objects.get(id = usuario.turma_id)
			except:
				turmas = Turma.objects.all()
				return render(request , 'usuario/principal/turma.php' ,locals())

			conteudos1 = Conteudo.objects.filter(linha_metro = 1, turma = usuario.turma);
			conteudos2 = Conteudo.objects.filter(linha_metro = 2,turma = usuario.turma);
			conteudos3 = Conteudo.objects.filter(linha_metro = 3,turma = usuario.turma);
			return render(request , 'usuario/principal/principal.php' ,locals())
	else:
		return HttpResponseRedirect('/login/')

def acertouPergunta(usuario_id, pergunta_id):
	perguntas_certas = Historico.objects.filter(usuario_id = usuario_id, acertou = True)
	for i in perguntas_certas:
		if i.pergunta_id == pergunta_id:
			return True
	return False

def getPerguntasErradas(usuario_id, conteudo_id):
	perguntas = Pergunta.objects.filter(conteudo_pertence = conteudo_id)
	perguntas_erradas = []
	for i in perguntas:
		enc = False
		for k in Historico.objects.filter(usuario_id = usuario_id, conteudo_id = conteudo_id, acertou = True): 
			if i.id == k.pergunta_id:
				enc = True
		if enc == False:
			perguntas_erradas.append(i)
	return perguntas_erradas 
		
def secundario(request, tema_conteudo):
	if request.user.is_authenticated():
		tema = transform_tema(tema_conteudo)
		usuario = Usuario.objects.get(username = request.user);
		try:
			conteudo = Conteudo.objects.get(tema = tema);
		except:
			return HttpResponseRedirect('/principal/')
		conteudo.descricao = conteudo.descricao

		if request.method == 'POST':
			if atualiza_historico( usuario.id ,usuario.turma_id,conteudo.id ,request.POST['pergunta_atual'] , request.POST['opcao'] ) == False:
				return render(request, 'usuario/avisos/sem_item_correto.php', locals())
			cont_all = Conteudo.objects.all()
			item  = Item.objects.get(id = request.POST['opcao'])

			#se o proximo for uma pergunta
			if item.possui_proxima_pergunta == True:
				if item.pergunta_proximo_id != None:
					pergunta = Pergunta.objects.get(id = item.pergunta_proximo_id);
					print "Entrou ja que e uma pergunta"
					if acertouPergunta(usuario.id, pergunta.id):
						print "Pergunta ja respondida e esta certa"
						perguntas_erradas = getPerguntasErradas(usuario.id, conteudo.id)
						if(len(perguntas_erradas) == 0 ):
							return render(request , 'usuario/avisos/conteudo_terminado.php' ,locals())
						else:
							pergunta_atual_id = pergunta.id;
							pergunta = perguntas_erradas.pop();
							while pergunta_atual_id == pergunta.id and len(perguntas_erradas)>1 :
								pergunta = perguntas_erradas.pop();
				else:
					perguntas_erradas = getPerguntasErradas(usuario.id, conteudo.id)
					if(len(perguntas_erradas) == 0 ):
						return render(request , 'usuario/avisos/conteudo_terminado.php' ,locals())
					else:
						pergunta_atual_id = pergunta.id;
						pergunta = perguntas_erradas.pop();
						while pergunta_atual_id == pergunta.id and len(perguntas_erradas)>1 :
							pergunta = perguntas_erradas.pop();


				itens = Item.objects.filter(pergunta_pertence = pergunta.id)


				atualiza_estado(usuario.id,conteudo.id, pergunta.id);
			#agora se for um conteudo
			else:
				pergunta = Pergunta.objects.get(id = request.POST['pergunta_atual']);
				perguntas_erradas = getPerguntasErradas(usuario.id, conteudo.id)
				if(len(perguntas_erradas) > 0):
					pergunta_atual_id = pergunta.id;
					pergunta = perguntas_erradas.pop()
					while pergunta_atual_id == pergunta.id and len(perguntas_erradas)>1 :
						pergunta = perguntas_erradas.pop();

					itens = Item.objects.filter(pergunta_pertence = pergunta.id)
				else:
					return render(request , 'usuario/avisos/conteudo_terminado.php' ,locals())
		else:
			try:
				estado = (Estado_Usuario.objects.get(usuario_id = usuario.id , conteudo_id = conteudo.id) )
				pergunta = Pergunta.objects.get(id = estado.pergunta_id)
			except:
				try:
					pergunta = Pergunta.objects.get(id = conteudo.pergunta_inicial_id)
				except:
					#caso nao exista uma pergunta iniciao no conteudo
					perguntas_erradas = getPerguntasErradas(usuario.id, conteudo.id)
					if len(perguntas_erradas) == 0:
						return render(request, 'usuario/avisos/sem_perguntas.php', locals())
					else:
						pergunta = perguntas_erradas.pop();
			if acertouPergunta(usuario.id, pergunta.id):
				perguntas_erradas = getPerguntasErradas(usuario.id, conteudo.id)
				if(len(perguntas_erradas) == 0 ):
					return render(request , 'usuario/avisos/conteudo_terminado.php' ,locals())
				else:
					pergunta_atual_id = pergunta.id;
					pergunta = perguntas_erradas.pop();
					while pergunta_atual_id == pergunta.id and len(perguntas_erradas)>1 :
						pergunta = perguntas_erradas.pop();

			itens = Item.objects.filter(pergunta_pertence = pergunta.id)

		pergunta.descricao = pergunta.descricao
		for it in itens:
			it.descricao = it.descricao
		return render(request , 'usuario/secundario/secundario.php' , locals())
	else:
		return HttpResponseRedirect('/login/')


def atualiza_estado_usuario(request, conteudo_id, pergunta_id):
	if request.user.is_authenticated():
		print "Conteudo Id = " + conteudo_id;
		usuario = Usuario.objects.get(username = request.user)
		conteudo = Conteudo.objects.get(id = conteudo_id)
		pergunta = Pergunta.objects.get(id = pergunta_id);
		try:
			item = Item.objects.get(id = pergunta.item_correto_id)
		except:
			perguntas_erradas = getPerguntasErradas(usuario.id, conteudo.id)
			if(len(perguntas_erradas) == 0 ):
				return HttpResponse("Conteudo Concluido!!!")
			else:
				pergunta_atual_id = pergunta.id;
				pergunta = perguntas_erradas.pop();
				while pergunta_atual_id == pergunta.id and len(perguntas_erradas)>1 :
					pergunta = perguntas_erradas.pop();
				atualiza_estado(usuario.id, conteudo_id, pergunta.id)
			return HttpResponse("Nao exite item correto na pergunta!!!")

		if item.possui_proxima_pergunta == False:
			perguntas_erradas = getPerguntasErradas(usuario.id, conteudo.id)
			if(len(perguntas_erradas) > 0):
				index = randrange(len(perguntas_erradas))
				while perguntas_erradas[index].id == pergunta.id and len(perguntas_erradas) != 1 :
					print "casa"
					index = randrange(len(perguntas_erradas))
				
				pergunta = perguntas_erradas.pop(index)

				itens = Item.objects.filter(pergunta_pertence = pergunta.id)
				atualiza_estado(usuario.id, conteudo_id, pergunta.id)
				return HttpResponse(request)
			else:
				return render(request , 'usuario/avisos/conteudo_terminado.php' ,locals())
		else:
			pergunta.id = item.pergunta_proximo_id;
			atualiza_estado(usuario.id, conteudo.id, pergunta.id)
			return secundario(request, conteudo.tema);
	else:
		return HttpResponseRedirect("/login/")


def atualiza_estado(usuario_id, conteudo_id, pergunta_id):
	usuario = Usuario.objects.get(id = usuario_id);
	try:
		estado = Estado_Usuario.objects.get(usuario_id = usuario_id , conteudo_id = conteudo_id)
		Estado_Usuario.objects.filter(id = estado.id).update(pergunta = pergunta_id)
	except:
		estado_usuario = Estado_Usuario.objects.create(
			usuario_id = usuario.id,
			turma_id = usuario.turma_id,
			conteudo_id = conteudo_id,
			pergunta_id = pergunta_id,
		);
		estado_usuario.save()

def atualiza_historico( id_usuario, id_turma, id_conteudo , id_pergunta, id_item):
	item = Item.objects.get(id = id_item)
	item_correto = (Pergunta.objects.get(id = id_pergunta) ).item_correto_id 
	if(item_correto == None):
		return False;
	resposta = None
	if item.id == item_correto:
		resposta = True
	else:
		resposta = False
	#aqui eu crio o historico
	historico = Historico.objects.create(
			usuario_id = id_usuario,
			turma_id = id_turma,
			conteudo_id = id_conteudo,
			pergunta_id = id_pergunta,
			item_id = id_item,
			acertou = resposta,
	)
	historico.save()
	return True

def estatisticas(request):
	if request.user.is_authenticated():
		usuario = Usuario.objects.get(username = request.user)
		return render(request, 'estatisticas/estatisticas.php', locals())
	else:
		return HttpResponseRedirect('/login/')


def verifica_respostas(request, id_conteudo, id_pergunta, id_item):
	if request.user.is_authenticated():
		try:
			conteudo = Conteudo.objects.get(id = id_conteudo)
			pergunta = Pergunta.objects.get(id = id_pergunta, conteudo_pertence_id = id_conteudo)
			item = Item.objects.get(id = id_item)
		except:
			return HttpResponse("FALSE")
		if(pergunta.item_correto_id == item.id):
			return HttpResponse("TRUE")
		else:
			return HttpResponse("FALSE")
	else:
		return HttpResponseRedirect('/login/')

def send_email(nome, email, msg):
	send_mail('AskMath', msg , email , ['saraiva.ufc@gmail.com'], fail_silently=False)

def contato(request):
	if request.method == 'POST':
		page = request.POST['page_atual']
		nome = None
		email = None
		msg = None
		try:
			nome = (request.POST['nome']).encode('utf-8', 'ignore')
			email = (request.POST['email']).encode('utf-8', 'ignore')
			msg = (request.POST['mensagem']).encode('utf-8', 'ignore')
		except:
			print "Falha ao enviar Email!!!"
			return HttpResponseRedirect(page)
		send_email(nome, email, msg)
		
		return HttpResponseRedirect(page)
	else:
		return HttpResponseRedirect('/login/')


def is_logado(request):
	if request.user.is_authenticated():
		return HttpResponse("1")
	else:
		return HttpResponse("0")


def transform_tema(t):
	tema =""
	for i in t:
		if i == '_':
			tema = tema + " "
		else:
			tema = tema + i
	return tema


def getAjuda(request, item_id):
	if request.user.is_authenticated():
		try:
			item = Item.objects.get(id = item_id);
		except:
			return HttpResponse("None");
		try:
			ajuda = Ajuda.objects.get(id = item.ajuda_proximo_id);
		except:
			return HttpResponse("None");

		return HttpResponse(ajuda.descricao);
	else:
		return HttpResponseRedirect('/login/')

def busca_ajuda(request, id_pergunta, id_item):
	if request.user.is_authenticated():
		usuario = Usuario.objects.get(username = request.user)
		busca = Busca_Ajuda.objects.create(
			usuario_id = usuario.id,
			pergunta_id = id_pergunta,
			item_id = id_item
		)
		busca.save()
		return HttpResponse("200")
		
	else:
		return HttpResponseRedirect('/login/')

def pulo(request,id_conteudo, id_pergunta):
	if request.user.is_authenticated():
		try:
			usuario = Usuario.objects.get(username = request.user)
		except:
			return HttpResponse("500");
		pulo = Pulo.objects.create(
			turma_id = usuario.turma_id,
			usuario_id = usuario.id,
			conteudo_id = id_conteudo,
			pergunta_id = id_pergunta
		)
		pulo.save()
		return HttpResponse("200")
		
	else:
		return HttpResponseRedirect('/login/')
