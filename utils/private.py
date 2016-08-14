traceMe = False
def trace(*args):
	if traceMe: print('[' + ' '.join(map(str, args)) + ']')

def Private(*privates):
	def onDecorator(aClass):
		class onInstance:
			def __init__(self, *args, **kargs):
				self.wrapped = aClass(*args, **kargs)
			def __getattr__(self, attr):
				trace('get:', attr)
				if attr in privates:
					raise TypeError('private attribute fetch: ' + attr)
				else:
					return getattr(self.wrapped, attr)
			def __setattr__(self, attr, value):
				trace('set:', attr, value)
				if attr == 'wrapped':
					self.__dict__[attr] = value
				elif attr in privates:
					raise TypeError('private attribute change: ' + attr)
				else:
					setattr(self.wrapped, attr, value)
		return onInstance
	return onDecorator

@Private('nome')
class Casa:
	def __init__(self):
		self.nome = "Ciano"
		
c = Casa()
print c.nome
