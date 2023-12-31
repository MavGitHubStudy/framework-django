# Generated by Django 4.2.4 on 2023-09-06 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seminar2app', '0003_categorymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('date_of_publication', models.DateField(auto_now_add=True)),
                ('number_of_views', models.IntegerField(default=0)),
                ('published', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seminar2app.authormodel')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='seminar2app.categorymodel')),
            ],
            options={
                'ordering': ['-date_of_publication'],
            },
        ),
    ]
