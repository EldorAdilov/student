# Generated by Django 5.0.2 on 2024-02-07 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_rename_username_myuser_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='phone_number',
            new_name='username',
        ),
    ]
