# Generated by Django 4.2.4 on 2023-09-13 10:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seminar2app', '0004_articlemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='date_of_publication',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]