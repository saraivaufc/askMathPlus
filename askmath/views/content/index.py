from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


def index_view(request):
    return HttpResponseRedirect(reverse('askmath:content_discipline_view'))
