# -*- coding: utf-8 -*-

#IMPORTS PYTHON
from __future__ import unicode_literals
import re
from random import randrange
import smtplib
try:
	from hashlib import md5
except:
	from md5 import new as md5
from email.mime.text import MIMEText

#IMPORTS DJANGO
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login as login_admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login as login_view
from django.contrib.auth.views import logout as logout_sys

#IMPORTS SPIRIT


#IMPORTS USER_PROFILE_SPIRIT

#IMPORTS ASK
from ask.forms.user import LoginForm
from ask.utils import *
from ask.models import *

def index(request):
	if request.user.is_authenticated() and request.user.is_moderator == False:
		return HttpResponseRedirect('/principal/')
	else:
		return HttpResponseRedirect('/login/')

def login(request, **kwargs):
	if request.user.is_authenticated():
		if request.user.is_moderator == False:
			return HttpResponseRedirect('/principal/')
		else:
			return HttpResponseRedirect('/principal_admin/')

	if request.method == "POST":
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			login_admin(request, user)
			return login(request)
		else:
			return render(request , 'login/login_falha.php' , locals())
	else:
		return login_view(request, authentication_form=LoginForm, **kwargs)

def login_falha(request):
	return render(request , 'login/login_falha.php' , locals())

@login_required
def logout(request):
	if request.user.is_moderator == False:
		try:
			usuario = Usuario.objects.get(username = request.user)
		except:
			return HttpResponseRedirect('/login/')
		fecharSecaoaberta(usuario)
	logout_sys(request)
	return HttpResponseRedirect('/login/')

def criarConta(request):
	if request.method == 'POST':

		deuErro = False;
		errors = []

		res = Usuario.objects.filter(email = request.POST['email'])
		if len(res) > 0:
			deuErro = True
			errors.append("Email ja existe.")

		res = Usuario.objects.filter(username = request.POST['username'])
		if len(res) > 0:
			deuErro = True
			errors.append("Nome de Usuario ja existe.")

		if deuErro:
			return render(request , 'cadastro/criarContaFalha.php',locals())

		try:
			user = Usuario.objects.create(
				username = request.POST['username'],
				email = request.POST['email'],
				first_name = request.POST['first_name'],
				last_name = request.POST['last_name'],
				password = md5(request.POST['password'] ).hexdigest(),
			)
			user.save()
			return render(request , 'cadastro/criarContaSucesso.php', locals())
		except:
			deuErro = True
			errors.append("Problemas no Banco de Dados.")
			return render(request , 'cadastro/criarContaFalha.php', locals())
	return render(request , 'cadastro/criarConta.php' , locals())

@login_required
def principal(request):
	if request.user.is_moderator == True:
		return HttpResponseRedirect("/principal_admin/")
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

		conteudos1 = Conteudo.objects.filter(linha_metro = 1, turma = usuario.turma).order_by("tema");
		conteudos2 = Conteudo.objects.filter(linha_metro = 2,turma = usuario.turma).order_by("tema");
		conteudos3 = Conteudo.objects.filter(linha_metro = 3,turma = usuario.turma).order_by("tema");

		fecharSecaoaberta(usuario)
		
		return render(request , 'usuario/principal/principal.php' ,locals())

@login_required
def secundario(request, tema_conteudo):
	if request.user.is_moderator == True:
		print 'casa'
		return HttpResponseRedirect("/principal_admin/" + tema_conteudo + "/")

	tema = transform_tema(tema_conteudo)
	try:
		usuario = Usuario.objects.get(username = request.user)
	except:
		return HttpResponseRedirect('/login/falha')
	try:
		conteudo = Conteudo.objects.get(tema = tema);
	except:
		return HttpResponseRedirect('/principal/')


	#DETALHES
	pulosRealizados = conteudo.getQuantPulosRealizados(usuario)
	vezesPediuAjuda = conteudo.getVezesPediuAjuda(usuario)
	pontosAcumulados = conteudo.getQuantPontos(usuario)

	if conteudo.getQuantPerguntasTotal() == len(conteudo.getPerguntasCertas(usuario)) and len(conteudo.getPerguntasRespondidas(usuario)) > 0:
		return conteudoTerminado(request, locals())

	if conteudo.getQuantPerguntasTotal() == len(conteudo.getPerguntasCertas(usuario)) and len(conteudo.getPerguntasRespondidas(usuario)) == 0:
		return render(request, 'usuario/avisos/sem_perguntas.php', locals())


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
			pontosAcumulados = conteudo.getQuantPontos(usuario)

		#agora se ele errou a pergunta
		else:
			pergunta.errou(usuario)

		#Se pergunta nao tiver uma proxima pergunta
		if pergunta.pergunta_proximo == None:
			perguntas_erradas = conteudo.getPerguntasRestantes(usuario)

			# Se nao Existir mais nenhma pergunta errada, e porque todas estao respondidas
			if len(perguntas_erradas ) == 0:
				print 'Conteudo Terminado Com Exito : linha 154'
				return conteudoTerminado(request, locals())
			# mas se ainda existir pergunta que nao foram respondidas ou estao erradas
			else:
				while len(perguntas_erradas) > 0:
					p = perguntas_erradas.pop()
					if p.id != pergunta.id:
						pergunta = p
						break

		#Mas se Ele tiver uma Pergunta Proxima
		else:
			pergunta = Pergunta.objects.get(id = pergunta.pergunta_proximo_id)
			perguntas_certas = conteudo.getPerguntasCertas(usuario)
			respondida_certa = False
			for i in perguntas_certas:
				if i.id == pergunta.id:
					respondida_certa = True
			if respondida_certa:
				perguntasRestantes = conteudo.getPerguntasRestantes(usuario)
				if len(perguntasRestantes) > 0:
					pergunta = perguntasRestantes[0]
				else:
					return conteudoTerminado(request, locals())



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
				
				if len(perguntas_erradas) == 0:
					return conteudoTerminado(request, locals())
				else:
					pergunta = perguntas_erradas.pop()

	#Isso Sempre e executa
	if len(conteudo.getPerguntasRestantes(usuario)) == 0:
		print 'Conteudo Terminado Com Exito : linha 215'
		return conteudoTerminado(request, locals())
		
	
	try:
		estado = Estado_Usuario.objects.filter(usuario = usuario.id, conteudo = conteudo.id)[0]
		Estado_Usuario.objects.filter(id = estado.id).update(pergunta = pergunta.id)
		print 'Conteguiu Econtrar o Estado_Usuario linha 199'
	except:
		print 'Erro ao buscar Estado_Usuario linha 202'

		atualiza_estado(usuario.id,conteudo.id, pergunta.id)

	itens = Item.objects.filter(pergunta_pertence = pergunta.id)
	print 'Response Padrao Caso nao Entre no Post : linha 206'

	try:
		his = Historico.objects.all()[0]
		print 'Historico Recente', len(his.getRecente(usuario, conteudo))
	except:
		pass

	
	perguntasTotal = (conteudo.getQuantPerguntasTotal())
	pulosRealizados = conteudo.getQuantPulosRealizados(usuario)
	pulosDisponiveis = conteudo.getQuantPulosRestantes(usuario)
	perguntasRestantes = len(conteudo.getPerguntasRestantes(usuario))
	perguntasCertas = len(conteudo.getPerguntasCertas(usuario))
	perguntasPuladas = len(conteudo.getPerguntasPuladas(usuario))
	pontosAcumulados = conteudo.getQuantPontos(usuario)
	perguntasSaltadas = conteudo.getPerguntasPuladasExclude(usuario, pergunta.id)
	try:
		pulosMaximo = (Pontuacao.objects.get(usuario = usuario.id,
											   conteudo = conteudo.id)).pulosMaximo
	except:
		pulosMaximo = conteudo.max_pulos

	existePular = False
	if pulosDisponiveis > 0:
		existePular	= True		

	existePulos = False
	if len(perguntasSaltadas) > 0:
		existePulos = True

	existeAjuda = False
	if pergunta.ajuda != None:
		existeAjuda = True

	try:
		secao = Secao.objects.get(usuario_id = usuario.id, 
								  conteudo_id = conteudo.id,
								  fim = None)
	except:
		print 'Nao Existe secao Aberta'
		secao = Secao.objects.create(usuario_id = usuario.id, conteudo_id = conteudo.id)
		secao.save()


	ps = []
	try:
		pergunta_inicial = Pergunta.objects.get(id = conteudo.pergunta_inicial_id)
		ps.append(pergunta_inicial)
		while ps[len(ps)-1].pergunta_proximo_id != None:
			pergunta_proximo = Pergunta.objects.get(id = ps[len(ps)-1].pergunta_proximo_id)
			ps.append(pergunta_proximo)
	except:
		return render(request , 'usuario/secundario/secundario.php' , locals())

	


	NUMEROPERGUNTA = 0
	achou = False
	for i in ps:
		if i.id == pergunta.id:
			NUMEROPERGUNTA += 1
			achou = True
			break;
		else:
			NUMEROPERGUNTA += 1
	if not achou:
		NUMEROPERGUNTA = 0


	return render(request , 'usuario/secundario/secundario.php' , locals())


@login_required
def secundarioOpcoes(request, tema_conteudo):
	if request.user.is_moderator == True:
		return HttpResponseRedirect("/principal_admin/" + tema_conteudo + "/")

	tema = transform_tema(tema_conteudo)
	try:
		usuario = Usuario.objects.get(username = request.user)
	except:
		return HttpResponseRedirect('/login/falha')
	try:
		conteudo = Conteudo.objects.get(tema = tema);
	except:
		return HttpResponseRedirect('/principal/')

	#DETALHES
	pulosRealizados = conteudo.getQuantPulosRealizados(usuario)
	vezesPediuAjuda = conteudo.getVezesPediuAjuda(usuario)
	pontosAcumulados = conteudo.getQuantPontos(usuario)
	if conteudo.getQuantPerguntasTotal() == len(conteudo.getPerguntasCertas(usuario)) and len(conteudo.getPerguntasRespondidas(usuario)) > 0:
		return conteudoTerminado(request, locals())

	if conteudo.getQuantPerguntasTotal() == len(conteudo.getPerguntasCertas(usuario)) and len(conteudo.getPerguntasRespondidas(usuario)) == 0:
		return render(request, 'usuario/avisos/sem_perguntas.php', locals())



	if request.method == 'POST':
		pass
	else:
		existePulos = False
		if len(conteudo.getPerguntasPuladas(usuario)) > 0:
			existePulos = True
		respondeuPergunta = False
		if len(conteudo.getPerguntasRespondidas(usuario)) > 0:
			respondeuPergunta = True

		perguntasSaltadas = conteudo.getPerguntasPuladas(usuario)
		fecharSecaoaberta(usuario)
		return render(request, 'usuario/secundario/secundarioOpcoes.php', locals())

@login_required
def secundarioEncerrar(request, tema_conteudo):
	if request.user.is_moderator == True:
		return HttpResponseRedirect("/principal_admin/" + tema_conteudo + "/")

	tema = transform_tema(tema_conteudo)
	try:
		usuario = Usuario.objects.get(username = request.user)
	except:
		return HttpResponseRedirect('/login/falha')
	try:
		conteudo = Conteudo.objects.get(tema = tema);
	except:
		return HttpResponseRedirect('/principal/')


	if request.method == 'POST':
		pass
	else:
		pulosRealizados = conteudo.getQuantPulosRealizados(usuario)

		questoesCorretas = len(conteudo.getPerguntasCertas(usuario))

		questoesErradas = len(conteudo.getPerguntasErradas(usuario))

		vezesPediuAjuda = conteudo.getVezesPediuAjuda(usuario)

		pontosAcumulados = conteudo.getQuantPontos(usuario)
		

		fecharSecaoaberta(usuario)
		return render(request, 'usuario/secundario/secundarioEncerrar.php', locals())


def fecharSecaoaberta(usuario):
	try:
		secao = Secao.objects.filter(usuario = usuario.id).order_by('-inicio');
		if len(secao) > 0:
			if secao[0].fim == None:
				print "Secao Fechada"
				secao[0].terminou()
	except:
		print "Falha ao fechar a secao"

@login_required
def conteudoTerminado(request, vars):
	fecharSecaoaberta(vars['usuario'])
	return render(request, 'usuario/avisos/conteudo_terminado.php', vars)

@login_required
def irPergunta(request, pergunta_id):
	if request.user.is_authenticated():
		if request.user.is_moderator == True:
			return HttpResponseRedirect("/login/")
		try:
			usuario = Usuario.objects.get(username = request.user)
		except:
			return HttpResponseRedirect('/login/falha')
		try:
			pergunta = Pergunta.objects.get(id = pergunta_id)
			conteudo = Conteudo.objects.get(id = pergunta.conteudo_pertence_id)
		except:
			return HttpResponseRedirect('/principal/')

		atualiza_estado(usuario.id, conteudo.id, pergunta.id)
		return HttpResponseRedirect("/principal/" + transform_tema_revert(conteudo.tema))

	else:
		return HttpResponseRedirect('/login/')

def acertouPergunta(usuario_id, pergunta_id):
	perguntas_certas = Historico.objects.filter(usuario_id = usuario_id, acertou = True)
	for i in perguntas_certas:
		if i.pergunta_id == pergunta_id:
			return True
	return False

@login_required
def atualiza_estado_usuario(request, conteudo_id, pergunta_id):
	if request.user.is_moderator == True:
		return HttpResponseRedirect("/login/")

	try:
		usuario = Usuario.objects.get(username = request.user)
	except:
		return HttpResponseRedirect('/login/falha')
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
	if pergunta.pergunta_proximo_id == None:
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
					pergunta = p
					break


	#Mas se Ele tiver uma Pergunta Proxima
	else:
		pergunta = Pergunta.objects.get(id = pergunta.pergunta_proximo_id)

	atualiza_estado(usuario.id, conteudo.id, pergunta.id)
	return HttpResponseRedirect("/principal/" +  transform_tema_revert(conteudo.tema))

def atualiza_estado(usuario_id, conteudo_id, pergunta_id):
	try:
		usuario = Usuario.objects.get(id = usuario_id)
	except:
		return HttpResponseRedirect('/login/falha')
	c = Conteudo.objects.get(id = conteudo_id)

	if len(c.getPerguntasRestantes(usuario)) == 0:
		return None

	certo = False
	for i in c.getPerguntasCertas(usuario):
		if i.id == pergunta_id:
			certo = True

	if certo:
		return

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

@login_required
def verifica_respostas(request, id_conteudo, id_pergunta, id_item):
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

def send_email(nome, email, msg):
	try:
		send_mail('AskMath', msg , email , ['saraiva.ufc@gmail.com'], fail_silently=False)
	except:
		return None

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
		if request.user.is_moderator == True:
			return HttpResponseRedirect("0")
		return HttpResponse("1")
	else:
		return HttpResponse("0")

@login_required
def getAjuda(request, pergunta_id):
	try:
		pergunta = Pergunta.objects.get(id = pergunta_id);
	except:
		return HttpResponse("None");
	try:
		ajuda = Ajuda.objects.get(id = pergunta.ajuda_id);
	except:
		return HttpResponse("None");

	return HttpResponse( string_to_latex(ajuda.descricao));

@login_required
def busca_ajuda(request, id_conteudo, id_pergunta):
	if request.user.is_moderator == True:
		return HttpResponseRedirect("/login/")
	usuario = Usuario.objects.get(username = request.user)
	busca = Busca_Ajuda.objects.create(
		usuario_id = usuario.id,
		conteudo_id = id_conteudo,
		pergunta_id = id_pergunta,
	)
	busca.save()
	return HttpResponse("200")


@login_required
def pulo(request,id_conteudo, id_pergunta):
	if request.user.is_moderator == True:
		return HttpResponseRedirect("/login/")
	try:
		usuario = Usuario.objects.get(username = request.user)
	except:
		return HttpResponseRedirect('/login/falha')
	
	pulo = Pulo.objects.create(
		turma_id = usuario.turma_id,
		usuario_id = usuario.id,
		conteudo_id = id_conteudo,
		pergunta_id = id_pergunta
	)
	pulo.save()
	try:
		conteudo = Conteudo.objects.get(id = id_conteudo)
	except:
		return HttpResponse("500")

	conteudo.declementaPulosRestantes(usuario)
	return HttpResponse("200")

@login_required
def ganhou_bonus(request, id_conteudo):
	if request.user.is_moderator == True:
		return HttpResponseRedirect("/login/")
	try:
		usuario = Usuario.objects.get(username = request.user)
	except:
		return HttpResponseRedirect('/login/falha')
	
	pontuacao = None
	try:
		pontuacao = Pontuacao.objects.get(usuario_id = usuario.id, conteudo_id = id_conteudo)
	except:
		return HttpResponse("False")

	if pontuacao.ganhou_bonus == True:
		Pontuacao.objects.filter(id = pontuacao.id).update(ganhou_bonus = False)
		return HttpResponse("True")
	else:
		return HttpResponse("False")


#errors
def my_custom_bad_request_view(request):
	return HttpResponse("Mal")

def my_custom_permission_denied_view(request):
	return HttpResponse("Acesso Negado")

def my_custom_page_not_found_view(request):
	return HttpResponse("Nao encontrado")

def my_custom_error_view(request):
	return HttpResponse("Erros nas views")
