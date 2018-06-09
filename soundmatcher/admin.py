from django.contrib import admin

from .models import Recording, Search, Match

admin.site.register(Recording)
admin.site.register(Search)
admin.site.register(Match)