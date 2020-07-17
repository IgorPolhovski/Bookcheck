from django.urls import path
from .views import BookView
from .views import BookCreateview
from .views import Bookbyid
app_name = "books"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('books/', BookView.as_view()),
    path('books/<int:id>/', Bookbyid.as_view()),
    path('books/create/', BookCreateview.as_view()),
]