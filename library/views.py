from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'library/home.html', context)

def about(request):
    return HttpResponse('<h1>About</h1>')
