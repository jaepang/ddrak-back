# Generated by Django 3.1.2 on 2020-10-17 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ddrakCalendar', '0005_auto_20201017_2314'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='endTime',
            new_name='end',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='startTime',
            new_name='start',
        ),
    ]
