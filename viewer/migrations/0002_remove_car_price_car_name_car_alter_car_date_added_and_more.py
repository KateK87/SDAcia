# Generated by Django 4.1.1 on 2024-08-30 14:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='price',
        ),
        migrations.AddField(
            model_name='car',
            name='name_car',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='car',
            name='year_of_manufature',
            field=models.CharField(max_length=4),
        ),
    ]
