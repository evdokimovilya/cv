from django.shortcuts import render


def index(request):
    template = 'page/index.html'

    return render(request, template)
