import random

from django.core.management.base import BaseCommand
from seminar2app.models import CategoryModel
# from ...models import CategoryModel


class Command(BaseCommand):
    help = "Create fake category."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Category ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            category = CategoryModel(name=f'Category{i}')
            category.save()
            self.stdout.write(f'{category}')
