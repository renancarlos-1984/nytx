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

def GetLatestOverview():
    #Returns latest Overview 4 Top Best Sellers
    url = 'https://api.nytimes.com/svc/books/v3/lists/overview.json'
    return MakeAPIQuery(url)

def GetLatestList(book_cat):
    #Returns latest Best sellers for given category
    url = 'https://api.nytimes.com/svc/books/v3/lists/' + book_cat
    return MakeAPIQuery(url)

def MakeAPIQuery(url):
    #Executes the API query and convert to JSON format
    full_url = url + '?api-key=' + API_KEY
    req = requests.get(full_url)
    reply = req.json()
    RecordAPIQuery(url, reply)
    return reply
    
    