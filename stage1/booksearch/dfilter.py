from django_filters import rest_framework as filters
from .models import Book


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class TitleFilter(filters.FilterSet):
    title = CharFilterInFilter(field_name='Book_title', lookup_expr='in')


    class Meta:
        model = Book
        fields = ['title']








