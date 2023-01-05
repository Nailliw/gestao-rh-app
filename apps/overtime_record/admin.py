from django.contrib import admin

# Register your models here.
from apps.overtime_record.models import OvertimeRecord

admin.site.register(OvertimeRecord)
