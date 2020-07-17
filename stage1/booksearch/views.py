from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from .serializers import BookbyidSerializer
from .serializers import BookCreateSerializer
from django.http import JsonResponse


class BookView(APIView):
    def get(self, request):
        books = Book.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = BookSerializer(books, many=True)
        return Response({"books": serializer.data})

class Bookbyid(APIView):
    def article_by_id(self, request, id):
        result = Book.objects.filter(id=id)
        serializer1 = BookbyidSerializer(result, many=True)
        return Response({"result": serializer1.data})

    def get(self, request, id):
        return self.article_by_id(self, id)

class BookCreateview(generics.CreateAPIView):
        serializer_class = BookCreateSerializer







