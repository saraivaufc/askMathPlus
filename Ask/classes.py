#-*- encoding=utf-8 -*-

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