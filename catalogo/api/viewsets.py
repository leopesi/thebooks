from rest_framework import viewsets
from catalogo.api import serializers
from catalogo import models


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorsSerializer

class BooksViewSet(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BooksSerializer
