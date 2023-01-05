from django.contrib import admin

# Register your models here.
from apps.collaborator.models import Collaborator

admin.site.register(Collaborator)
