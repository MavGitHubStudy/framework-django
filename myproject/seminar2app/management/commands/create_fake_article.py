import random

from django.core.management.base import BaseCommand
from seminar2app.models import ArticleModel, AuthorModel, CategoryModel
# from ...models import ArticleModel


class Command(BaseCommand):
    help = "Create fake article."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count of article')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            _author = AuthorModel.objects.filter(pk=i).first()
            _category = CategoryModel.objects.filter(pk=i).first()
            article = ArticleModel(title=f'Title{i}',
                                   content=f'Content{i}',
                                   date_of_publication='2000-01-01',
                                   author=_author,
                                   category=_category,
                                   number_of_views=random.randint(1,
                                                                  1000),
                                   published=random.randint(0, 1))
            article.save()
            self.stdout.write(f'{article}')
