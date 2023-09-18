# Generated by Django 4.2.4 on 2023-09-17 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seminar5app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seminar5app.articlemodel', verbose_name='Статья')),
            ],
        ),
    ]
