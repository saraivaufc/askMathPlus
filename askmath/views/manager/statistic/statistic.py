#-*- encoding=UTF-8 -*-


from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .istatistic import IStatistic

class Statistic(IStatistic):
	
	@method_decorator(login_required)
	def choose_type(self, request):
		return render(request, "askmath/manager/statistic/manager_choose_types.html",
			{'request': request})