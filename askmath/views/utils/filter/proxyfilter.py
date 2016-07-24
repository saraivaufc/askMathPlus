from askmath.entities import TextMessage
from askmath.views.index import ProxyHome
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .filter import Filter
from .ifilter import IFilter


class ProxyFilter(IFilter):
    def __init__(self):
        self.__filter = Filter()

    def search(self, request):
        if request.method == "POST":
            try:
                expression = request.POST['search']
                if len(expression) <= 100:
                    return self.__filter.search(request, expression)
                else:
                    messages.error(request, TextMessage.SEARCH_ERROR_SIZE)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR_FORM)
        return HttpResponseRedirect(reverse('askmath:home'))
