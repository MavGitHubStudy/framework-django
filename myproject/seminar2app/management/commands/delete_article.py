import random

from django.core.management.base import BaseCommand
from seminar2app.models import ArticleModel, AuthorModel, CategoryModel
# from ...models import ArticleModel


class Command(BaseCommand):
    help = "Delete article title by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='ArticleModel ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        article = ArticleModel.objects.filter(pk=pk).first()
        if article is not None:
            article.delete()
        self.stdout.write(f'Deleted {article}')

