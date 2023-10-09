from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(songs)
admin.site.register(album)
admin.site.register(language)
admin.site.register(playlist)

