from django.contrib import admin
from .models import Book, Author

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'second_name', 'get_num']
    def get_num(self, obj):
        return obj.book_set.count()
    get_num.short_description = 'Number of Books'
    get_num.admin_order_field = 'num_books'

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_author']
    def get_author(self, obj):
        return obj.author.first_name+' '+obj.author.second_name
    get_author.short_description = 'Author'
    get_author.admin_order_field = 'book__author'

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
