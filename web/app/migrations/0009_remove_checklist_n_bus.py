# Generated by Django 4.1.1 on 2023-01-09 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_checklist_n_bus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checklist',
            name='n_bus',
        ),
    ]