# Generated by Django 5.0.2 on 2024-02-08 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0016_delete_uploadedfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='image',
            field=models.FileField(upload_to='vid/'),
        ),
    ]
