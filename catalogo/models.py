from django.db import models
from django.urls import reverse

class Genre(models.Model):
    """Model representando um gênero de livro."""
    name = models.CharField(max_length=70, help_text='Insira um gênero de livro (ex. Romance)')

    def __str__(self):
        """Retorna uma String representando o Model object."""
        return self.name

class Book(models.Model):
    """Model representando o livro."""
    title = models.CharField(max_length=70)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Descreva, com poucas palavras, o livro.')
    pages = models.CharField(max_length=13, help_text='Insira a quantidade de páginas')
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')

    def __str__(self):
        """Retorna uma String representando o Model object."""
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

class Author(models.Model):
    """Model representando o Autor."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Retorna uma url de acesso a um autor específico."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

    class Meta:
        ordering = ['last_name']