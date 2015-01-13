# -*- coding: utf-8 -*-

#IMPORTS PYTHON

#IMPORTS DJANGO

#IMPORTS SPIRIT

#IMPORTS USER_PROFILE_SPIRIT

#IMPORTS ASK

def transform_tema(t):
	tema =""
	for i in t:
		if i == '_':
			tema = tema + " "
		else:
			tema = tema + i
	return tema

def transform_tema_revert(t):
	tema =""
	for i in t:
		if i == ' ':
			tema = tema + "_"
		else:
			tema = tema + i
	return tema

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

def minimize_frase(text):
	quant = 0
	des = ""
	add = False
	for i in text:
		if quant < 50:
			des += i
			quant+=1
		else:
			add = True
			break
		
	if add:
		des +="..."
	return des