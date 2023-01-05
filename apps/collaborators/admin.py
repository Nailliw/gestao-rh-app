from django.contrib import admin

# Register your models here.
from apps.collaborators.models import Collaborator

admin.site.register(Collaborator)
