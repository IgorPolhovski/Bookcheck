from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.Serializer):
    id = serializers.CharField()
    title = serializers.CharField(max_length=120)
    author_name = serializers.CharField()

class Bookbyid(serializers.Serializer):
    id = serializers.CharField()
    author_name = serializers.CharField()
    title = serializers.CharField(max_length=120)
    description = serializers.CharField()


class BookbyidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'description', 'author_name')

class BooksearcherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'description', 'author_name')

class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'description', 'author_name')
