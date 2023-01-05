from django.db import models

# Create your models here.
from apps.collaborator.models import Collaborator


class Document(models.Model):
    description = models.CharField(max_length=200)
    owner = models.ForeignKey(Collaborator, on_delete=models.PROTECT)

    def __str__(self):
        return self.description
