from django.db import models

# Create your models here.
from apps.collaborator.models import Collaborator


class OvertimeRecord(models.Model):
    justification = models.CharField(max_length=200)
    owner = models.ForeignKey(Collaborator, on_delete=models.PROTECT)

    def __str__(self):
        return self.justification
