# Generated by Django 3.1.2 on 2020-10-17 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddrakCalendar', '0007_auto_20201017_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='daysOfWeek',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
