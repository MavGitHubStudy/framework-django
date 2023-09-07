import random

from django.core.management.base import BaseCommand
from seminar2app.models import ArticleModel, AuthorModel, CategoryModel
# from ...models import ArticleModel


class Command(BaseCommand):
    help = "Update  article title by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='ArticleModel ID')
        parser.add_argument('title', type=str, help='CategoryModel title')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        _title = kwargs.get('title')
        article = ArticleModel.objects.filter(pk=pk).first()
        article.title = _title
        article.save()
        self.stdout.write(f'{article}')
