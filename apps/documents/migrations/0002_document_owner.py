# Generated by Django 4.1.5 on 2023-01-05 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collaborator', '0002_collaborator_departments_collaborator_enterprise_and_more'),
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='collaborator.collaborator'),
        ),
    ]
