
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=64)
    author_name = models.CharField(max_length=64)
    description = models.TextField()


    def __str__(self):
        return self.title