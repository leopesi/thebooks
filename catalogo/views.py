from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Book, Author, Genre
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def index(request):
    """View function for home page of site."""
    num_books = Book.objects.all().count()
    authors = Author.objects.all().count()
    genre = Genre.objects.all().count()

    context = {
        'num_books': num_books,
        'num_authors': authors,
        'num_genre': genre,
    }
    return render(request, 'index.html', context=context)

class MyBookListView(generic.ListView):
    queryset = Book.objects.all()
    context_object_name = 'mybooks'
    template_name = 'mybooks.html'

class AuthorListView(generic.ListView):
    """Listar autores."""
    model = Author
    context_object_name = 'list_authors'
    paginate_by = 10
    def get_context_data(self, **kwargs):
        context = super(AuthorListView, self).get_context_data(**kwargs)
        context['some_data'] = 'This is just some data'
        return context

class AuthorDetailView(generic.DetailView):
    """Visualizar algum author detalhadamente."""
    model = Author
    #context_object_name = 'authors'
    #template_name = 'author_detail.html'

class AuthorCreate(generic.CreateView):
    """Criar um novo autor."""
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
    initial = {'date_of_death': '11/06/2020'}

class AuthorUpdate(generic.UpdateView):
    """Atualizar um cadastro de autor."""
    model = Author
    fields = '__all__'

class AuthorDelete(generic.DeleteView):
    """Deletar um cadastro de autor."""
    model = Author
    success_url = reverse_lazy('authors')


class BookListView(generic.ListView):
    """Listar livros."""
    model = Book
    context_object_name = 'list_books'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['some_data'] = 'This is just some data'
        return context

class BookDetailView(generic.DetailView):
    """Visualizar algum livro detalhadamente."""
    model = Book


class BookCreate(CreateView):
    model = Book
    fields = ['title', 'author', 'summary', 'pages', 'genre']
    permission_required = 'catalog.can_mark_returned'


class BookUpdate(UpdateView):
    model = Book
    fields = ['title', 'author', 'summary', 'pages', 'genre']
    permission_required = 'catalog.can_mark_returned'


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books')
    permission_required = 'catalog.can_mark_returned'