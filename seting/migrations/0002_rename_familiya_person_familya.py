# Generated by Django 5.0.1 on 2024-02-03 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seting', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='familiya',
            new_name='familya',
        ),
    ]
