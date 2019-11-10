from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('books/add', views.addBooks, name='add_books'),
    path('author/add', views.addAuthor, name='add_author'),
    path('books', views.allBooks, name='all_books'),
    path('books/<int:id>', views.book_details, name='book_details'),
    path('author/<int:id>', views.author_details, name='author_details'),
    path('authors', views.allAuthors, name='all_authors'),
    path('logout', views.logout_view, name='logout'),
]