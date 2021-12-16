import os
import requests
from .models import BooksRequest

API_KEY = os.environ.get('API_KEY_EVAR').strip()

def RecordAPIQuery(url, reply):
    error_message = ''
    #check if it was faulty
    if('fault' in reply.keys()):
        status = 'FAULT'
        error_message = reply['fault']['faultstring']
    else:
        status = reply['status']
        if(status == 'ERROR'):
            error_message = reply['errors'][0]
    api_query = BooksRequest.objects.create(
        query = url,
        status = status,
        error_message = error_message)
    return None

def MakeAPIQuery(url):
    #Executes the API query and convert to JSON format
    full_url = 'https://api.nytimes.com' + url + 'api-key=' + API_KEY
    req = requests.get(full_url)
    reply = req.json()
    RecordAPIQuery(url, reply)
    return reply

def GetLatestOverview():
    #Returns latest Overview 4 Top Best Sellers
    url = '/svc/books/v3/lists/overview.json?'
    return MakeAPIQuery(url)

def GetLatestList(book_cat):
    #Returns latest Best sellers for given category
    url = '/svc/books/v3/lists/' + book_cat + '?'
    return MakeAPIQuery(url)
    
def GetBookFromCategory(book_cat, book_title):
    #Send the book information for the book detail page
    latest_list = GetLatestList(book_cat)
    display_cat = latest_list['results']['display_name']
    for book in latest_list['results']['books']:
        if(book['title'] == book_title):
            return display_cat, book

def GetBookHistory(book_title):
    #Get the book Ranking history from another API call
    url = '/svc/books/v3/lists/best-sellers/history.json?title=' + \
        book_title + '&'
    return MakeAPIQuery(url)
