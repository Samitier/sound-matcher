from django.contrib import admin

from .models import Recording, Search

admin.site.register(Recording)
admin.site.register(Search)