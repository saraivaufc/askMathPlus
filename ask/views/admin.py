# -*- coding: utf-8 -*-

#IMPORTS PYTHON
from __future__ import unicode_literals
try:
	from hashlib import md5
except:
	from md5 import new as md5
import re
from random import randrange
import smtplib
from email.mime.text import MIMEText
import json


#IMPORTS DJANGO
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

#IMPORTS SPIRIT

#IMPORTS USER_PROFILE_SPIRIT

#IMPORTS ASK
from ask.models import *
from ask.utils import *
from ask.forms import *





@login_required
def principal_admin(request):
	if request.user.is_moderator == True:
		usuario = User.objects.get(username = request.user)

		conteudos1 = Conteudo.objects.filter(linha_metro = 1).order_by("tema");
		conteudos2 = Conteudo.objects.filter(linha_metro = 2).order_by("tema");
		conteudos3 = Conteudo.objects.filter(linha_metro = 3).order_by("tema");
		return render(request, "admin/principal_admin/principal_admin.php", locals())
	else:
		return HttpResponseRedirect("/principal/")

@login_required
def secundario_admin(request, tema_conteudo):
	if request.user.is_moderator == True:
		tema = transform_tema(tema_conteudo)
		usuario = User.objects.get(username = request.user)
		try:
			conteudo = Conteudo.objects.get(tema = tema)
		except:
			return HttpResponseRedirect("/principal_admin/")
		turmas = conteudo.turma.all()

		try:
			pergunta_inicial = Pergunta.objects.get(id = conteudo.pergunta_inicial_id)
		except:
			pass

		return render(request, "admin/secundario_admin/secundario_admin.php", locals())

	else:
		return HttpResponseRedirect("/principal/"+ tema_conteudo)

@login_required
def terciario_admin(request, tema_conteudo, id_pergunta):
	if request.user.is_moderator == True:
		tema = transform_tema(tema_conteudo)
		usuario = User.objects.get(username = request.user)
		try:
			conteudo = Conteudo.objects.get(tema = tema)
			pergunta = Pergunta.objects.get(id = id_pergunta)
		except:
			return HttpResponseRedirect("/principal_admin/")

		existeAnterior = False
		existeProximo = False
		existeAjuda = False
		try:
			perguntaAnterior = Pergunta.objects.get(pergunta_proximo_id = pergunta.id)
			existeAnterior = True
		except:
			existeAnterior = False
		try:
			perguntaProximo = Pergunta.objects.get(id = pergunta.pergunta_proximo_id)
			existeProximo = True
		except:
			existeProximo = False
		try:
			ajuda = Ajuda.objects.get(id = pergunta.ajuda_id)
			existeAjuda = True
		except:
			existeAjuda = False

		return render(request, "admin/terciario_admin/terciario_admin.php", locals())

	else:
		return HttpResponseRedirect("/principal/"+ tema_conteudo)


@login_required
def gerenciador(request):
	usuario = User.objects.get(username = request.user)
	return render(request, "admin/gerenciador/principal/principal.php", locals())


@login_required
def listOpcao(request, opcao):
	if opcao == "1":
		turmas = Turma.objects.all()
		return  render(request, "admin/gerenciador/opcao/turma/list.php", locals())
	elif opcao == "2":
		conteudos = Conteudo.objects.all()
		return  render(request, "admin/gerenciador/opcao/licao/list.php", locals())
	elif opcao == "3":
		perguntas = Pergunta.objects.all()
		return  render(request, "admin/gerenciador/opcao/pergunta/list.php", locals())
	elif opcao == "4":
		ajudas = Ajuda.objects.all()
		return  render(request, "admin/gerenciador/opcao/ajuda/list.php", locals())
	elif opcao == "5":
		itens = Item.objects.all()
		return  render(request, "admin/gerenciador/opcao/item/list.php", locals())
	elif opcao == "6":
		deficiencias = Deficiencia.objects.all()
		return  render(request, "admin/gerenciador/opcao/deficiencia/list.php", locals())
	else:
		return HttpResponseRedirect("/gerenciador/")

@login_required
def addOpcao(request, opcao):
	try:
		opcao = int(opcao)
	except:
		return HttpResponseRedirect("/gerenciador/")

	my_template = 'admin/gerenciador/opcao/opcao.php'

	if request.method == "POST":
		if opcao == 1:
			form = TurmaForm(request.POST)
		elif opcao == 2:
			form = ConteudoForm(request.POST)
		elif opcao == 3:
			return salvarPergunta(request)
		else:
			return  HttpResponseRedirect("/gerenciador/")

		if form.is_valid():
			print "Formulario Valido"
			if(form.save()):
				ok = True
				return render(request, "admin/gerenciador/opcao/avisos/adicionado.php", locals())
			else:
				ok = False
				return render(request, "admin/gerenciador/opcao/avisos/adicionado.php", locals())
		else:
			ok = False
			return render(request, "admin/gerenciador/opcao/avisos/adicionado.php", locals())
	else:
		if opcao == 1:
			form = PartialTurmaForm()
		elif opcao == 2:
			form = PartialConteudoForm()
		elif opcao == 3:
			form = PartialPerguntaForm()
			return render(request, "admin/gerenciador/opcao/pergunta/add.php", locals())
		else:
			return HttpResponseRedirect("/gerenciador/")

		return  render(request, "admin/gerenciador/opcao/add/add.php", locals())

@login_required
def remOpcao(request, opcao, id):
	try:
		opcao = int(opcao)
	except:
		return HttpResponse("Opcao nao e numeral")

	try:
		if opcao == 1:
			Turma.objects.filter(id = id).delete()
		elif opcao == 2:
			Conteudo.objects.filter(id = id).delete()
		elif opcao == 3:
			Pergunta.objects.filter(id = id).delete()
		else:
			return HttpResponseRedirect("/gerenciador/")
		return HttpResponse("True")
	except:
		return HttpResponse("False")


@login_required
def editOpcao(request, opcao, id):
	try:
		opcao = int(opcao)
	except:
		return HttpResponseRedirect("/gerenciador/")

	my_template = 'admin/gerenciador/opcao/opcao.php'

	try:
		if opcao == 1:
			turma = Turma.objects.get(id = id)
		elif opcao == 2:
			conteudo = Conteudo.objects.get(id = id)
		elif opcao == 3:
			pergunta = Pergunta.objects.get(id = id)
		else:
			return HttpResponseRedirect("/gerenciador/")
	except:
		return HttpResponseRedirect("/gerenciador/")

	if request.method == 'POST':
		if opcao == 1:
			form = TurmaForm(request.POST,instance=turma)
		elif opcao == 2:
			form = ConteudoForm(request.POST,instance=conteudo)
		elif opcao == 3:
			form = PerguntaForm(request.POST,instance=pergunta)
		else:
			return HttpResponseRedirect("/gerenciador/")               

		if form.is_valid():
			form.save()
			ok= True
			return render(request, "admin/gerenciador/opcao/avisos/editado.php", locals())
		else:
			ok = False
			return render(request, "admin/gerenciador/opcao/avisos/editado.php", locals())
	else:
		if opcao == 1:
			form = PartialTurmaForm(instance=turma)
		elif opcao == 2:
			form = PartialConteudoForm(instance=conteudo)
		elif opcao == 3:
			form = PartialPerguntaForm(instance=pergunta)
		else:
			return HttpResponseRedirect("/gerenciador/")

		return render(request, 'admin/gerenciador/opcao/edit/edit.php', locals())

def ordenaPerguntas(request):
	if request.method == "POST":
		conteudo_id = request.POST['conteudo']
		perguntas = request.POST['perguntas']


		perguntas = json.loads(perguntas)
		
		if len(perguntas) == 0:
			Conteudo.objects.filter(id = conteudo_id).update(pergunta_inicial_id = None)
			return HttpResponse("Sem Perguntas Iniciais")
		
		quant_perguntas = len(perguntas.keys())

		for  i in range(quant_perguntas):
			pergunta_id = perguntas[str(i)]
			if i == 0:
				Conteudo.objects.filter(id = conteudo_id).update(pergunta_inicial_id = pergunta_id)
			else:
				pergunta_anterior_id = perguntas[str(i-1)]
				Pergunta.objects.filter(id = pergunta_anterior_id ).update(pergunta_proximo_id = pergunta_id)
				if i == (quant_perguntas-1):
					Pergunta.objects.filter(id = pergunta_id).update(pergunta_proximo_id = None)




	return HttpResponse("Success")


def zerarPerguntas(request):
	print "casaquista"
	if request.method == "POST":
		conteudo_id = request.POST['conteudo']
		perguntas = request.POST['perguntas']


		perguntas = json.loads(perguntas)

		quant_perguntas = len(perguntas.keys())

		for  i in range(quant_perguntas):
			pergunta_id = perguntas[str(i)]
			Pergunta.objects.filter(id = pergunta_id).update(pergunta_proximo_id = None)




	return HttpResponse("Success")


def salvarPergunta(request):
	try:
		conteudo = Conteudo.objects.get(id = request.POST['conteudo_pertence'])
	except:
		print "Erro ao pegar Conteudo"
		conteudo = None

	try:
		descricao = request.POST['descricao']
	except:
		print "Erro ao pegar Descricao"
		descricao = " "

	try:
		pontos = request.POST['pontos']
	except:
		print "Erro ao Pegar Pontos"
		pontos = 0


	item_a_existe = False
	try:
		item_a = request.POST['item_a']
	except:
		print "Erro ao pegar Item A"
		item_a = None
	if len(item_a) > 0 and item_a != None:
		try:
			deficiencia_a = request.POST['deficiencia_a']
		except:
			print "Erro ao Pegar Deficiencia A"
			deficiencia_a = None
		try:
			try:
				d_a = Deficiencia.objects.create(descricao = deficiencia_a)
				d_a.save()
				deficiencia_a = d_a.id
			except:
				print "Erro ao salvar Deficiencia A"
				deficiencia_a = None
			try:
				i_a = Item.objects.create(descricao = item_a, deficiencia = deficiencia_a)
				i_a.save()
				item_a_existe = True
				item_a = i_a.id
			except:
				print "Erro ao salver item A"
				item_a = None
		except:
			print "Erro ao Salvar Item A"
			item_a = None
	else:
		item_a  = None
	
	item_b_existe = False
	try:
		item_b = request.POST['item_b']
	except:
		print "Erro ao pegar Item B"
		item_b = None
	if len(item_b) > 0 and item_b != None:
		try:
			deficiencia_b = request.POST['deficiencia_b']
		except:
			print "Erro ao Pegar Deficiencia B"
			deficiencia_b = None
		try:
			try:
				d_b = Deficiencia.objects.create(descricao = deficiencia_b)
				d_b.save()
				deficiencia_b = d_b.id
			except:
				print "Erro ao salvar Deficiencia B"
				deficiencia_b = None
			try:
				i_b = Item.objects.create(descricao = item_b, deficiencia = deficiencia_b)
				i_b.save()
				item_b_existe = True
				item_b = i_b.id
			except:
				print "Erro ao salver item B"
				item_b = None
		except:
			print "Erro ao Salvar Item b"
			item_b = None
	else:
		item_b = None


	item_c_existe = False
	try:
		item_c = request.POST['item_c']
	except:
		print "Erro ao pegar Item C"
		item_c  = None
	if len(item_c) > 0 and item_c != None:
		try:
			deficiencia_c = request.POST['deficiencia_c']
		except:
			print "Erro ao Pegar Deficiencia C"
			deficiencia_c = None
		try:
			try:
				d_c = Deficiencia.objects.create(descricao = deficiencia_c)
				d_c.save()
				deficiencia_c = d_c.id
			except:
				print "Erro ao salvar Deficiencia C"
				deficiencia_c = None
			try:
				i_c = Item.objects.create(descricao = item_c, deficiencia = deficiencia_c)
				i_c.save()
				item_c_existe = True
				item_c = i_c.id
			except:
				print "Erro ao salver item C"
				i_c = None
		except:
			print "Erro ao salvar Item c"
			item_c = None

	item_d_existe = False
	try:
		item_d = request.POST['item_d']
	except:
		print "Erro ao pegar Item D"
		item_d = None
	if len(item_d) > 0 and item_d != None:
		try:
			deficiencia_d = request.POST['deficiencia_d']
		except:
			print "Erro ao Pegar Deficiencia D"
			deficiencia_d = None
		try:
			try:
				d_d = Deficiencia.objects.create(descricao = deficiencia_d)
				d_d.save()
				deficiencia_d = d_d.id
			except:
				print "Erro ao salvar Deficiencia D"
				deficiencia_d = None
			try:
				i_d = Item.objects.create(descricao = item_d, deficiencia = deficiencia_d)
				i_d.save()
				item_d_existe = True
				item_d = i_d.id
			except:
				print "Erro ao salver item D"
				item_d = None
			
		except:
			print "Erro ao salvar Item D"
			item_d = None

	item_e_existe = False
	try:
		item_e = request.POST['item_e']
	except:
		print "Erro ao pegar Item E"
		item_e = None
	if len(item_e) > 0 and item_e != None:
		try:
			deficiencia_e = request.POST['deficiencia_e']
		except:
			print "Erro ao Pegar Deficiencia E"
			deficiencia_e = None
		try:
			try:
				d_e = Deficiencia.objects.create(descricao = deficiencia_e)
				d_e.save()
				deficiencia_e = d_e.id
			except:
				print "Erro ao salvar Deficiencia E"
				deficiencia_e = None
			try:
				i_e = Item.objects.create(descricao = item_e)
				i_e.save()
				item_e_existe = True
				item_e = i_e.id
			except:
				print "Erro ao salver item E"
				item_e = None
			
		except:
			print "Erro ao salvar Item E"
			item_e = None


	ajuda_existe = False
	try:
		ajuda = request.POST['ajuda']
	except:
		print "Erro ao pegar Ajuda"
		ajuda = None
	
	if len(ajuda) > 0 and ajuda != None:
		try:
			a = Ajuda.objects.create(descricao = ajuda)
			a.save()
			ajuda_existe = True
			ajuda = a.id
		except:
			print "Erro ao salvar Ajuda"
			ajuda = None
	else:
		ajuda = None

	try:
		item_correto = request.POST['item_correto']
	except:
		print "Erro ao pegar Item Correto"
		item_correto = None

	if item_correto != None:
		if item_correto == 'a' and item_a_existe:
			item_correto = item_a
		elif item_correto == 'b' and item_b_existe:
			item_correto = item_b
		elif item_correto == 'c' and item_c_existe:
			item_correto = item_c
		elif item_correto == 'd' and item_d_existe:
			item_correto = item_d
		if item_correto == 'e' and item_e_existe:
			item_correto = item_e
		else:
			item_correto = None


	print conteudo
	print '\n'
	print descricao
	print '\n'
	print pontos
	print '\n'
	print item_a, item_b, item_c, item_d, item_e
	print '\n'
	print item_correto
	print '\n'
	print ajuda
	pergunta = Pergunta.objects.create(
				conteudo_pertence = conteudo,
				descricao = descricao,
				pontos = pontos,
				item_a = item_a,
				item_b = item_b,
				item_c = item_c,
				item_d = item_d,
				item_e = item_e,
				item_correto = item_correto,
				ajuda = ajuda,
			)
	pergunta.save()

	try:
		try:
			pass		
		except:
			print "Erro ao salvr Pergunta"
		ok = True
		opcao = 3
		return render(request, "admin/gerenciador/opcao/avisos/adicionado.php", locals())
	except:
		ok = False
		opcao = 3
		return render(request, "admin/gerenciador/opcao/avisos/adicionado.php", locals())