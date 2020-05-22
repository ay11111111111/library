from django.db import models
from django.urls import reverse
DEFAULT_AUTHOR_ID = 1

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)


    def __str__(self):
        return self.first_name + ' ' + self.second_name

    def get_absolute_url(self):
        return reverse('book-create')


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('library-home')
