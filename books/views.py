from django.shortcuts import render
from .books_api_functions import GetLatestOverview, GetLatestList
from .books_api_functions import GetBookFromCategory, GetBookHistory
from django.http import JsonResponse

def BooksOverview(request):
    template_name = 'books/books_overview.html'
    context = {}
    context['latest_overview'] = GetLatestOverview()
    return render(request, template_name, context)

def BooksList(request, book_cat:str):
    template_name = 'books/books_list.html'
    context = {}
    context['latest_list'] = GetLatestList(book_cat)
    #request.session['book_cat'] = book_cat
    return render(request, template_name, context)

def BookDetail(request, book_cat:str, book_title:str):
    template_name = 'books/book_detail.html'
    context = {}
    context['book_cat'] = book_cat
    context['latest_list'] = GetLatestList(book_cat)
    context['display_cat'], \
        context['book'] = GetBookFromCategory(book_cat, book_title)
    context['book_hist'] = GetBookHistory(book_title)
    #print(GetBookHistory(book_title))
    return render(request, template_name, context)

def BookDetailAJAX(request, book_cat:str, book_title:str):
    data = {}
    data['book_cat'] = book_cat
    data['latest_list'] = GetLatestList(book_cat)
    data['display_cat'], \
        data['book'] = GetBookFromCategory(book_cat, book_title)
    return JsonResponse(data)