from django.db import models

#Record all Book API requests
class BooksRequest(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    query = models.CharField(max_length=25)
    status = models.CharField(max_length=10)
    error_message = models.CharField(max_length=250)

    def __str__(self):
        return self.query