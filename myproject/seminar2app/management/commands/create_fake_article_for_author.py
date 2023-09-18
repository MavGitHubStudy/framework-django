import random
from datetime import datetime

from django.core.management.base import BaseCommand
from seminar2app.models import ArticleModel, AuthorModel, CategoryModel
from seminar2app.utils import get_random_date
# from ...models import ArticleModel


class Command(BaseCommand):
    help = "Create fake article."

    def add_arguments(self, parser):
        parser.add_argument('article', type=int, help='Number of article')
        parser.add_argument('author', type=int, help='Number of author')

    def handle(self, *args, **kwargs):
        _num_title = kwargs.get('article')
        _num_author = kwargs.get('author')

        _author = AuthorModel.objects.filter(pk=_num_author).first()
        _category = CategoryModel.objects.filter(pk=random.randint(1, 10)).first()
        # datetime(year, month, day, hour, minute, second, microsecond)
        start_dt = datetime(2023, 1, 1, 0, 0, 0, 0)
        end_dt = datetime.now()

        article = ArticleModel(title=f'Title{_num_title}',
                               content=f'Content{_num_title}',
                               date_of_publication=get_random_date(start_dt, end_dt),
                               author=_author,
                               category=_category,
                               number_of_views=random.randint(1,
                                                              1000),
                               published=random.randint(0, 1))
        article.save()
        self.stdout.write(f'{article}')
