from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from .models import *


def home(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'library/home.html', context)

class PostCreateView(CreateView):
    model = Book
    fields = ['author', 'title']

def about(request):
    return HttpResponse('<h1>About</h1>')
