from django.shortcuts import render


def index_view(request):
    return render(request, 'askmath/manager/manager_home.html', {'request': request})
