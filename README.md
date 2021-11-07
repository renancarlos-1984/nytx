# nytx
The New York Times API web-app

To replicate this app locally:

1 Provide the environmental variables as below:
- API_KEY_EVAR = 'get your api key at developer.nytimes.com'
- SECRET_KEY_EVAR = 'create a secret key for django'
- DEBUG_EVAR = 'True' #for development environment only
- ALLOWED_HOSTS_EVAR = '*' #for development environment only
- DATABASE_EVAR = '{"ENGINE": "django.db.backends.sqlite3", "NAME": "db.sqlite3"}' #to use local sqlite3 database

2 Makemigrations

3 Migrate

Follow the evolution of this app in nytx.herokuapp.com
