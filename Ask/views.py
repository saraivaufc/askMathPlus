# -*- encoding=utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from Ask.models import *
from django.core.mail import send_mail
try:
	from hashlib import md5
except:
	from md5 import new as md5

import re
from random import randrange
import smtplib
from email.mime.text import MIMEText
from django.contrib.auth.views import login as login_view
from spirit.forms.user import LoginForm
from django.contrib.auth.views import logout as logout_sys
from spirit.utils.ratelimit.decorators import ratelimit
from django.test import Client
from classes import *
from utils import *

def index(request):
	if request.user.is_authenticated() and request.user.is_moderator == False:
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
		#try:
		user = Usuario.objects.create(
			username = request.POST['username'],
			email = request.POST['email'],
			first_name = request.POST['first_name'],
			last_name = request.POST['last_name'],
			password = md5(request.POST['password'] ).hexdigest(),
		)
		user.save()
		return render(request , 'cadastro/criarContaSucesso.php', locals())
		#except:
		#	return render(request , 'cadastro/criarContaFalha.php', locals())
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
		
def secundario(request, tema_conteudo):
	if request.user.is_authenticated():
		tema = transform_tema(tema_conteudo)
		usuario = Usuario.objects.get(username = request.user);
		try:
			conteudo = Conteudo.objects.get(tema = tema);
		except:
			return HttpResponseRedirect('/principal/')

		#Se nao existir nenhuma pergunta no conteudo
		if conteudo.getQuantPerguntasTotal == 0:
			print 'Sem Perguntas: linha 129'
			return render(request, 'usuario/avisos/sem_perguntas.php', locals())

		if len(conteudo.getPerguntasNaoRespondidas(usuario)) == 0:
			print 'Conteudo Terminado Com Exito: linha 123'
			return render(request, 'usuario/avisos/conteudo_terminado.php', locals())

		try:
			pontuacao = UsuarioPontuacao.objects.get(usuario = usuario.id, conteudo = conteudo.id)
		except:
			pontuacao = UsuarioPontuacao.objects.create(usuario_id = usuario.id,
														conteudo_id = conteudo.id,
														pulosRestantes = conteudo.max_pulos)
			pontuacao.save()


		if request.method == 'POST':
			pergunta = Pergunta.objects.get(id = request.POST['pergunta_atual'])

			#Caso a Pergunta nao tenha um item Correto(Falha do Administrador)
			if atualiza_historico( usuario.id ,usuario.turma_id,conteudo.id ,pergunta.id , request.POST['opcao'] ) == False:
				print 'Sem Item Correto : linha 139'
				return render(request, 'usuario/avisos/sem_item_correto.php', locals())
			
			cont_all = Conteudo.objects.all()
			item  = Item.objects.get(id = request.POST['opcao'])
			# Se Ele Respondeu a Pergunta Corretamente
			if pergunta.item_correto_id == item.id:

				#atualizando a pontuacao
				pergunta.acertou(usuario)

				print 'acertou'
				#Se Mesmo Acertando, a pergunta nao tiver uma proxima pergunta
				if pergunta.pergunta_proximo_acertou == None:
					perguntas_erradas = conteudo.getPerguntasRestantes(usuario)

					# Se nao Existir mais nenhma pergunta errada, e porque todas estao respondidas
					if len(perguntas_erradas) == 0:
						print 'Conteudo Terminado Com Exito : linha 154'
						return render(request, 'usuario/avisos/conteudo_terminado.php', locals())

					# mas se ainda existir pergunta que nao foram respondidas ou estao erradas
					else:
						while len(perguntas_erradas) > 0:
							p = perguntas_erradas.pop()
							if p.id != pergunta.id:
								pergunta = p
								break


				#Mas se Ele tiver uma Pergunta Proxima
				else:
					pergunta = Pergunta.objects.get(id = pergunta.pergunta_proximo_acertou_id)
					if len(conteudo.getPerguntasRestantes) == 0:
						print 'Conteudo Terminado Com Exito : linha 169'
						return render(request, 'usuario/avisos/conteudo_terminado.php', locals())
					else:
						#Se a pergunta ja estiver sido respondidade corretaente
						try:
							his = Historico.objects.get(usuario = usuario.id,
											 	 conteudo = conteudo.id,
											 	 pergunta = pergunta.id,
												  acertou = True,)
							pergunta = c.getPerguntasRestantes(usuario)[0]
						#se a pergunta ainda nao tiver sido respondidade corretamente
						except:
							print "Pulei para a proxima"

			#Se Ele Nao Respondeu A Pergunta Corretamente
			else:
				#Se Mesmo Errando, a pergunta nao tiver uma proxima pergunta
				if pergunta.pergunta_proximo_errou == None:
					perguntas_erradas = getPerguntasErradas(usuario.id, conteudo.id)

					while len(perguntas_erradas) > 1:
						p = perguntas_erradas.pop()
						if p.id != pergunta.id:
							pergunta = p
							break

				#Mas se Ele tiver uma Pergunta Proxima
				else:
					pergunta = Pergunta.objects.get(id = pergunta.pergunta_proximo_errou_id)


		# Se o Metodo nao for Post
		else:
			#Ele tenta ir para a ultima pergunta que nao tinha respondido
			try:
				estado = (Estado_Usuario.objects.get(usuario_id = usuario.id , conteudo_id = conteudo.id) )
				pergunta = Pergunta.objects.get(id = estado.pergunta_id)
			
			#caso ele nao consiga(seja porque nunca tenha respondido nenhuma questao)
			except:
				
				#Ele tenta ir para a primeira pergunta que esta setada no conteudo
				try:
					pergunta = Pergunta.objects.get(id = conteudo.pergunta_inicial_id)
				
				#caso nao exista uma pergunta iniciao no conteudo(Nao foi setada)
				except:
					perguntas_erradas = conteudo.getPerguntasRestantes(usuario)
					
					if len(conteudo.getPerguntasRestantes(usuario)) == 0:
						return render(request, 'usuario/avisos/conteudo_terminado.php', locals())
					else:
						pergunta = perguntas_erradas.pop()

		#Isso Sempre e executa
		if len(conteudo.getPerguntasNaoRespondidas(usuario)) == 0:
			print 'Conteudo Terminado Com Exito : linha 215'
			return render(request, 'usuario/avisos/conteudo_terminado.php', locals())
		
		try:
			estado = Estado_Usuario.objects.filter(usuario = usuario.id, conteudo = conteudo.id)[0]
			Estado_Usuario.objects.filter(id = estado.id).update(pergunta = pergunta.id)
			print 'Conteguiu Econtrar o Estado_Usuario linha 220'
		except:
			print 'Erro ao buscar Estado_Usuario linha 222'

			atualiza_estado(usuario.id,conteudo.id, pergunta.id)

		itens = Item.objects.filter(pergunta_pertence = pergunta.id)
		print 'Response Padrao Caso nao Entre no Post : linha 227'

		try:
			his = Historico.objects.all()[0]
			print 'Historico Recente', len(his.getRecente(usuario, conteudo))
		except:
			pass

		
		print 'Detalhe'
		perguntasTotal = (conteudo.getQuantPerguntasTotal())
		pulosRealizados = conteudo.getQuantPulosRealizados(usuario)
		pulosDisponiveis = conteudo.getQuantPulosRestantes(usuario)
		perguntasRespondidas = len(conteudo.getPerguntasRespondidas(usuario))
		perguntasNaoRespondidas = len(conteudo.getPerguntasNaoRespondidas(usuario))
		perguntasRestantes = len(conteudo.getPerguntasRestantes(usuario))
		perguntasCertas = len(conteudo.getPerguntasCertas(usuario))
		perguntasErradas = len(conteudo.getPerguntasErradas(usuario))
		perguntasPuladas = len(conteudo.getPerguntasPuladas(usuario))
		vezPediuAjuda = conteudo.getVezesPediuAjuda(usuario)
		pontos = conteudo.getQuantPontos(usuario)

		return render(request , 'usuario/secundario/secundario.php' , locals())
	else:
		return HttpResponseRedirect('/login/')


def secundarioOpcoes(request, tema_conteudo):
	if request.user.is_authenticated():

		tema = transform_tema(tema_conteudo)
		usuario = Usuario.objects.get(username = request.user);
		try:
			conteudo = Conteudo.objects.get(tema = tema);
		except:
			return HttpResponseRedirect('/principal/')


		if request.method == 'POST':
			pass
		else:
			existePulos = False
			if len(conteudo.getPerguntasPuladas(usuario)) > 0:
				existePulos = True
			respondeuPergunta = False
			if len(conteudo.getPerguntasRespondidas(usuario)) > 0:
				respondeuPergunta = True

			return render(request, 'usuario/secundario/secundarioOpcoes.php', locals())
	else:
		return HttpResponseRedirect('/login/')


def secundarioEncerrar(request, tema_conteudo):
	if request.user.is_authenticated():

		tema = transform_tema(tema_conteudo)
		usuario = Usuario.objects.get(username = request.user);
		try:
			conteudo = Conteudo.objects.get(tema = tema);
		except:
			return HttpResponseRedirect('/principal/')


		if request.method == 'POST':
			pass
		else:
			questoesPuladas = len(conteudo.getPerguntasPuladas(usuario))

			questoesCorretas = len(conteudo.getPerguntasCertas(usuario))

			questoesErradas = len(conteudo.getPerguntasErradas(usuario))

			vezesPediuAjuda = conteudo.getVezesPediuAjuda(usuario)
			
			return render(request, 'usuario/secundario/secundarioEncerrar.php', locals())
	else:
		return HttpResponseRedirect('/login/')

def acertouPergunta(usuario_id, pergunta_id):
	perguntas_certas = Historico.objects.filter(usuario_id = usuario_id, acertou = True)
	for i in perguntas_certas:
		if i.pergunta_id == pergunta_id:
			return True
	return False

def atualiza_estado_usuario(request, conteudo_id, pergunta_id):
	if request.user.is_authenticated():
		usuario = Usuario.objects.get(username = request.user)
		conteudo = Conteudo.objects.get(id = conteudo_id)
		pergunta = Pergunta.objects.get(id = pergunta_id);
		
		#tento pegar o item correto da questao
		try:
			item = Item.objects.get(id = pergunta.item_correto_id)
		
		#Se a questao nao tiver um item correto
		except:
			perguntas_erradas = conteudo.getPerguntasNaoRespondidas(usuario)
			if(len(perguntas_erradas) == 0 ):
				return HttpResponse("Conteudo Concluido!!!")
			else:
				while len(perguntas_erradas)>0 :
					p = perguntas_erradas.pop();
					if p.id != pergunta.id:
						pergunta = p
						break
				atualiza_estado(usuario.id, conteudo_id, pergunta.id)
			return HttpResponse("None")

		#Se Mesmo Acertando, a pergunta nao tiver uma proxima pergunta
		if pergunta.pergunta_proximo_acertou == None:
			perguntas_erradas =  conteudo.getPerguntasRestantes(usuario)

			# Se nao Existir mais nenhma pergunta errada, e porque todas estao respondidas
			if len(perguntas_erradas) == 0:
				print 'Conteudo Terminado Com Exito : linha 298'
				return render(request, 'usuario/avisos/conteudo_terminado.php', locals())

			# mas se ainda existir pergunta que nao foram respondidas ou estao erradas
			else:
				while len(perguntas_erradas) > 0:
					p = perguntas_erradas.pop()
					if p.id != pergunta.id:
						print 'buceta'
						pergunta = p
						break


		#Mas se Ele tiver uma Pergunta Proxima
		else:
			pergunta = Pergunta.objects.get(id = pergunta.pergunta_proximo_acertou_id)

		atualiza_estado(usuario.id, conteudo.id, pergunta.id)
		return HttpResponseRedirect("/principal/" +  transform_tema_revert(conteudo.tema))

	else:
		return HttpResponseRedirect("/login/")


def atualiza_estado(usuario_id, conteudo_id, pergunta_id):
	usuario = Usuario.objects.get(id = usuario_id)
	c = Conteudo.objects.get(id = conteudo_id)

	if len(c.getPerguntasRestantes(usuario)) == 0:
		return None

	certo = False
	for i in c.getPerguntasCertas(usuario):
		if i.id == pergunta_id:
			certo = True

	if certo:
		return


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


def getAjuda(request, pergunta_id):
	if request.user.is_authenticated():
		try:
			pergunta = Pergunta.objects.get(id = pergunta_id);
		except:
			return HttpResponse("None");
		try:
			ajuda = Ajuda.objects.get(id = pergunta.ajuda_id);
		except:
			return HttpResponse("None");

		return HttpResponse( string_to_latex(ajuda.descricao));
	else:
		return HttpResponseRedirect('/login/')

def busca_ajuda(request, id_conteudo):
	if request.user.is_authenticated():
		usuario = Usuario.objects.get(username = request.user)
		busca = Busca_Ajuda.objects.create(
			usuario_id = usuario.id,
			conteudo_id = id_conteudo,
		)
		busca.save()
		return HttpResponse("200")
		
	else:
		return HttpResponseRedirect('/login/')

def pulo(request,id_conteudo, id_pergunta):
	if request.user.is_authenticated():
		usuario = Usuario.objects.get(username = request.user)
		
		pulo = Pulo.objects.create(
			turma_id = usuario.turma_id,
			usuario_id = usuario.id,
			conteudo_id = id_conteudo,
			pergunta_id = id_pergunta
		)
		pulo.save()
		conteudo = Conteudo.objects.get(id = id_conteudo)
		conteudo.declementaPulosRestantes(usuario)
		return HttpResponse("200")
		
	else:
		return HttpResponse("500")

def string_to_latex(s):
	s+="."
	site = "http://latex.codecogs.com/png.latex?"
	res = ""
	index = 0;
	temp = ""
	iniciou = False
	terminou = False
	for i in s:
		if i == '$':
			if iniciou == True:
				iniciou = False;
				terminou = True
			else:
				iniciou = True
				continue
		if terminou:
			res += "<img src='" + site + temp +"'/>"
			terminou = False
			iniciou = False
			temp = ""
			continue

		if iniciou:
			temp +=i
		else:
			res += i

	print res
		
	return res




