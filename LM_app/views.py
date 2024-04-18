from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def context(request):
    return render(request, 'context.html')
