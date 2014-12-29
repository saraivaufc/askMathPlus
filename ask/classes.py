#-*- encoding=utf-8 -*-
from ask.models import *


class Est1():
	tema = None
	total = None
	respondidas = None
	certas = None
	erradas = None

	def __init__(self, tema, total,respondidas,certas, erradas):
		self.tema = tema
		self.total = total
		self.respondidas = respondidas
		self.certas = certas
		self.erradas = erradas

def getEst_1(usuario):
	conteudo = Conteudo.objects.filter(turma = usuario.turma)
	list = []

	for i in conteudo:
		tema = i.tema
		total = len( Pergunta.objects.filter(conteudo_pertence = i.id))
		respondidas = 0
		for k in Pergunta.objects.filter(conteudo_pertence = i.id):
			for t in Historico.objects.filter(pergunta = k.id, usuario = usuario.id):
				respondidas +=1
		certas = 0
		for k in Pergunta.objects.filter(conteudo_pertence = i.id):
			for t in Historico.objects.filter(pergunta = k.id, acertou = True, usuario = usuario.id):
				certas +=1
		erradas = respondidas - certas

		dic = Est1(tema,total,respondidas, certas,erradas)
		list.append(dic)		

	return list

class Est2():
	tema = None
	pulos = None

	def __init__(self, tema, pulos):
		self.tema = tema
		self.pulos = pulos


def getEst_2(usuario):
	conteudo = Conteudo.objects.filter(turma = usuario.turma)
	list = []
	for i in conteudo:
		tema = i.tema
		pulos = len(Pulo.objects.filter(usuario = usuario.id , turma = usuario.turma, conteudo = i.id))
		dic = Est2(tema, pulos)
		list.append(dic)
	return list	

