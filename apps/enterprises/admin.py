from django.contrib import admin

# Register your models here.
from apps.enterprises.models import Enterprise


admin.site.register(Enterprise)
