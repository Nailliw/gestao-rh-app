from django.db import models

# Create your models here.


class OvertimeRecord(models.Model):
    justification = models.CharField(max_length=200)

    def __str__(self):
        return self.justification
