# Generated by Django 3.2.4 on 2021-06-24 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0010_notification_centerid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='noti',
        ),
    ]
