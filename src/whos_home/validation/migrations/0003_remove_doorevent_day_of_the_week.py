# Generated by Django 4.1.3 on 2022-11-16 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('validation', '0002_doorevent_day_of_the_week'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doorevent',
            name='day_of_the_week',
        ),
    ]
