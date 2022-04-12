from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Book, Author, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    # The 'all()' is implied by default.
    authors = Author.objects.all().count()

    context = {
        'num_books': num_books,
        'num_authors': authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'list_books'
    paginate_by = 10
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context

class AuthorListView(generic.ListView):
    model = Author
    template_name = 'author_list.html'
    context_object_name = 'list_authors'
    paginate_by = 10
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(AuthorListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'

class AuthorDetailView(generic.DetailView):
    model = Author
    #context_object_name = 'authors'
    template_name = 'author_detail.html'