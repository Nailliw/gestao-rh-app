# Generated by Django 4.1.5 on 2023-01-05 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collaborator', '0003_alter_collaborator_user'),
        ('documents', '0002_document_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='collaborator.collaborator'),
            preserve_default=False,
        ),
    ]