from django.urls import path
from .views import BooksOverview, BooksList

app_name = 'books'
urlpatterns = [
    path('', BooksOverview, name='books_overview'),
    path('<str:book_cat>/', BooksList, name='books_list'),
]
