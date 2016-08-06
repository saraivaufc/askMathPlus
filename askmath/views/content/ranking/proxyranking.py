from askmath.entities import TextMessage
from askmath.models.classe import Classe as ClasseModel
from askmath.models.users import Student as StudentModel
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator

from .iranking import IRanking
from .ranking import Ranking

class ProxyRanking(IRanking):
	def __init__(self):
		self.__ranking = Ranking()

	@method_decorator(login_required)
	def view_ranking(self, request, id_classe = None):
		if request.user.has_perm("askmath.read_ranking") and request.user.has_perm("askmath.access_content"):
			try:
				classe = ClasseModel.objects.filter(id=id_classe, exists=True, visible=True)[0]
			except:
				classe = None
			try:
				student = request.user.get_person_class(request.user, StudentModel)
				return self.__ranking.view_ranking(request, student, classe)
			except Exception, e:
				print e
				messages.error(request, TextMessage.ERROR)
		else:
			messages.error(request, TextMessage.USER_NOT_PERMISSION)

		return HttpResponseRedirect(reverse('askmath:home'))
