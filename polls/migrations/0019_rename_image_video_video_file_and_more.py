# Generated by Django 5.0.2 on 2024-02-08 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_alter_video_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='image',
            new_name='video_file',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='name',
            new_name='video_name',
        ),
    ]