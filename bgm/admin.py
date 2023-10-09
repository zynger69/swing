from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(score)
admin.site.register(org_score)
admin.site.register(channel)