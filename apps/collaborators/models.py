from django.contrib.auth.models import User
from django.db import models
from apps.departments.models import Department
from apps.enterprises.models import Enterprise


class Collaborator(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departments = models.ManyToManyField(Department)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
