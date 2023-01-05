from django.contrib import admin

# Register your models here.
from apps.departments.models import Department

admin.site.register(Department)
