# Generated by Django 5.0.1 on 2024-02-07 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_delete_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='image',
            field=models.FileField(upload_to='videos/'),
        ),
    ]
