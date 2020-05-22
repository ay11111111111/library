from rest_framework import serializers
from ..models import *

class BookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    class Meta:
        model = Book
        fields = ('id', 'title', 'author')

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('first_name', 'second_name')

class BookCreateSerializer(serializers.ModelSerializer):
    author = AuthorSerializer
    class Meta:
        model = Book
        fields = ('title', 'author')
