import random

from django.core.management.base import BaseCommand
from seminar2app.models import ArticleModel, AuthorModel, CategoryModel
# from ...models import ArticleModel


class Command(BaseCommand):
    help = "Get all articles"

    # def add_arguments(self, parser):
    #     parser.add_argument('count', type=int, help='ArticleModel ID')

    def handle(self, *args, **kwargs):
        articles = ArticleModel.objects.all()
        self.stdout.write(f'{articles}')
