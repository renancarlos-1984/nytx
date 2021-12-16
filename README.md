# nytx.herokuapp.com
The New York Times API web-app

To replicate this app locally:

1. Provide the environmental variables as below:
- API_KEY_EVAR = 'get your api key at developer.nytimes.com'
- SECRET_KEY_EVAR = 'create a secret key for django'
- DEBUG_EVAR = 'True' #for development environment only
- ALLOWED_HOSTS_EVAR = '*' #for development environment only
- DATABASE_EVAR = '{"ENGINE": "django.db.backends.sqlite3", "NAME": "db.sqlite3"}' #to use local sqlite3 database

2. Makemigrations

3. Migrate

===============
Revision History

Rev 0.1: 28/Oct/2021
Learned how this specific API expects the query requests messages to be written so the engine can understand and process it. Understood how the replies are structured and translated the API engine answer into readable data.

Rev 0.2: 09/Nov/2021
Improved aesthetics and backend functionality, without any new features added. Used grid display for the responsive design instead of media queries. Created a model that records all the Books API requests and the responses status