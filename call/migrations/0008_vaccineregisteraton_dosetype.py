# Generated by Django 3.2.4 on 2021-06-22 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0007_vaccineregisteraton_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaccineregisteraton',
            name='doseType',
            field=models.BooleanField(default=True),
        ),
    ]