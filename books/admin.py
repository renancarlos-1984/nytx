from django.contrib import admin
from .models import BooksRequest

# Register your models here.

class BooksRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'datetime', 'query', 'status')

admin.site.register(BooksRequest, BooksRequestAdmin)
