# Generated by Django 3.1.2 on 2020-10-17 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddrakCalendar', '0006_auto_20201017_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='endTime',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='startTime',
            field=models.TimeField(blank=True, null=True),
        ),
    ]