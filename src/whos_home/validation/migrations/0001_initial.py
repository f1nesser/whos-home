# Generated by Django 4.1.3 on 2022-11-12 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DoorEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(verbose_name='datetime door opened')),
                ('action', models.CharField(choices=[('EN', 'entering'), ('LE', 'leaving')], max_length=2)),
                ('whos_there', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='validation.person')),
            ],
        ),
    ]
