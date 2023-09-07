import random

from django.core.management.base import BaseCommand
from seminar2app.models import ArticleModel, AuthorModel, CategoryModel
# from ...models import ArticleModel


class Command(BaseCommand):
    help = "Create  article."

    def add_arguments(self, parser):
        parser.add_argument('author', type=int, help='AuthorModel ID')
        parser.add_argument('category', type=int, help='CategoryModel ID')

    def handle(self, *args, **kwargs):
        _author = AuthorModel.objects.get(pk=kwargs.get('author'))
        _category = CategoryModel.objects.get(pk=kwargs.get('category'))

        article = ArticleModel(title=f'Title',
                               content=f'Content',
                               date_of_publication='2000-01-01',
                               author=_author,
                               category=_category,
                               number_of_views=random.randint(1,
                                                              1000),
                               published=random.randint(0, 1))
        article.save()
        self.stdout.write(f'done, article pk = {article.pk}')
