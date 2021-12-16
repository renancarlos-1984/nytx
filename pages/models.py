from django.db import models
import datetime

#Manager to show only published revision histories
class RevisionAbout(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(publish=True)

#Revision history to show in About
class RevisionHistory(models.Model):
    revision = models.CharField(max_length=10)
    releasedate = models.DateField(datetime.datetime.now)
    shortdescription = models.CharField(max_length=50)
    fulldescription = models.TextField()
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.shortdescription

    objects = models.Manager()
    about_objects = RevisionAbout()
