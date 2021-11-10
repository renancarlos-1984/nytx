from django.urls import path
from .views import AboutPage

app_name = 'pages'
urlpatterns = [
    path('about/', AboutPage, name='about'),
]