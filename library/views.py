from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from .models import *


def home(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'library/home.html', context)


class AuthorDetailView(DetailView):
    model = Author


class AuthorCreateView(CreateView):
    model = Author
    fields = ['first_name', 'second_name']


class AuthorUpdateView(UpdateView):
    model = Author
    fields = ['first_name', 'second_name']


class AuthorDeleteView(DeleteView):
    model = Author
    success_url = '/'


class BookDetailView(DetailView):
    model = Book


class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author']


class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author']


class BookDeleteView(DeleteView):
    model = Book
    success_url = '/'
