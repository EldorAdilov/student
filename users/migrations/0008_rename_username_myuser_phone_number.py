# Generated by Django 5.0.2 on 2024-02-07 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_rename_myuseer_myuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='username',
            new_name='phone_number',
        ),
    ]
