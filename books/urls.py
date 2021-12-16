from django.urls import path
from .views import BooksOverview, BooksList, BookDetail, BookDetailAJAX

app_name = 'books'
urlpatterns = [
    path('', BooksOverview, name='books_overview'),
    path('<str:book_cat>/', BooksList, name='books_list'),
    path('<str:book_cat>/<str:book_title>', BookDetail, name='book_detail'),
    path('aj/<str:book_cat>/<str:book_title>', BookDetailAJAX, name='book_detail_ajax')
]