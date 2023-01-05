from django.db import models

# Create your models here.


class Enterprise(models.Model):
    name = models.CharField(max_length=100, help_text='Enterprise name')

    def __str__(self):
        return self.name
