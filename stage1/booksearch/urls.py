from django.urls import path
from .views import BookCreateview, BookViewSet

app_name = "books"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('books/create/', BookCreateview.as_view()),
    path('books/', BookViewSet.as_view({'get': 'list'})),
    path('books/<int:id>/', BookViewSet.as_view({'get': 'article_by_id'})),

]