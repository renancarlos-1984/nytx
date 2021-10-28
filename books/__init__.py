import os
import requests

API_KEY = os.environ.get('API_KEY_EVAR').strip()

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
    return req.json()