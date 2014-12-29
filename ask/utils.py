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