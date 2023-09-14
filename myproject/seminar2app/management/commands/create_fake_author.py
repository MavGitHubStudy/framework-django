from django.core.management.base import BaseCommand
from seminar2app.models import AuthorModel
# from ...models import AuthorModel


class Command(BaseCommand):
    help = "Create fake author."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count of authors')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = AuthorModel(name=f'Name{i}',
                                 surname=f'Surname{i}',
                                 email=f'main{i}@mail.ru',
                                 biography=f'biography{i}',
                                 birthday=f'2000-01-01'
                                 )

            author.save()
            self.stdout.write(f'{author}')
