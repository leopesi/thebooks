from django.contrib import admin
from django.urls import path, include
from .views import index, BookListView, AuthorListView, BookDetailView, AuthorDetailView

urlpatterns = [
    path('/', index, name='index'),
    path('books/', BookListView.as_view(), name='books'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', AuthorDetailView.as_view(), name='author-detail'),
]
