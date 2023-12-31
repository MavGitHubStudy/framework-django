# Generated by Django 4.2.4 on 2023-09-06 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seminar2app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('biography', models.TextField(max_length=1000)),
                ('birthday', models.DateField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='gamemodel',
            options={'ordering': ['-played']},
        ),
    ]
