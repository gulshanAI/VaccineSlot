# Generated by Django 3.1.6 on 2021-06-20 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0002_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaccineregisteraton',
            name='for18',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='vaccineregisteraton',
            name='for45',
            field=models.BooleanField(default=True),
        ),
    ]
