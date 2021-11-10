from django.contrib import admin
from .models import RevisionHistory

# Register your models here.

class RevisionHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'revision', 'releasedate', 'shortdescription', 'publish')

admin.site.register(RevisionHistory, RevisionHistoryAdmin)