# Generated by Django 3.1.6 on 2021-06-20 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0004_auto_20210620_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='noti',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='ofDate',
            field=models.CharField(max_length=15),
        ),
    ]
