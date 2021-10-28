from django.shortcuts import render
from books import GetLatestOverview, GetLatestList

def BooksOverview(request):
    template_name = 'books/books_overview.html'
    context = {}
    context['latest_overview'] = GetLatestOverview()
    return render(request, template_name, context)

def BooksList(request, book_cat:str):
    template_name = 'books/books_list.html'
    context = {}
    context['latest_list'] = GetLatestList(book_cat)
    return render(request, template_name, context)