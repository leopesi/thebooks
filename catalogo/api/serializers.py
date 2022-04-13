from rest_framework import serializers
from catalogo import models

class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = '__all__'

class BooksSerializer(serializers.ModelSerializer):
    author = AuthorsSerializer(read_only=True)
    class Meta:
        model = models.Book
        fields = '__all__'

    def create(self, validated_data):
        author = self.context['request'].user
        new_post = models.Book.objects.create(author=author)
        return new_post

