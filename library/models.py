from django.db import models
from django.urls import reverse

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    num_books = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name + ' ' + self.second_name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('library-home')

    # def save(self, *args, **kwargs):
    #     super(Model, self).save(*args, **kwargs)
