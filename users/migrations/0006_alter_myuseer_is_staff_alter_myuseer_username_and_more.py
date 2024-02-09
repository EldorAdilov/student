# Generated by Django 5.0.1 on 2024-02-07 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_myuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuseer',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='myuseer',
            name='username',
            field=models.CharField(db_index=True, max_length=15, unique=True),
        ),
        migrations.DeleteModel(
            name='MyUser',
        ),
    ]
