import random
from datetime import datetime


from django.core.management.base import BaseCommand
from seminar3app.models import AuthorModel, CategoryModel, ArticleModel

LOREM = (f"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et "
         f"dolore magna aliqua. Massa tincidunt nunc pulvinar sapien et ligula ullamcorper. At volutpat diam ut "
         f"venenatis tellus in metus. Volutpat odio facilisis mauris sit amet massa vitae tortor condimentum. Eu sem "
         f"integer vitae justo. Mattis enim ut tellus elementum sagittis vitae et. Iaculis urna id volutpat lacus "
         f"laoreet non. Pretium lectus quam id leo in vitae turpis. Dolor sit amet consectetur adipiscing elit ut "
         f"aliquam purus. Eget arcu dictum varius duis at. Commodo ullamcorper a lacus vestibulum. Blandit volutpat "
         f"maecenas volutpat blandit aliquam etiam erat velit. In massa tempor nec feugiat nisl pretium. Urna "
         f"cursus eget nunc scelerisque viverra mauris. Vestibulum lectus mauris ultrices eros in cursus turpis. "
         f"Dui ut ornare lectus sit amet. Congue eu consequat ac felis donec et odio. Ut etiam sit amet nisl purus. "
         f"Tristique senectus et netus et. Quam elementum pulvinar etiam non quam lacus suspendisse.")


class Command(BaseCommand):
    help = "Generate fake authors and posts."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='count of user')

    def handle(self, *args, **kwargs):
        text = LOREM.split()
        count = kwargs.get('count')
        for k in range(1, count + 1):
            category = CategoryModel(name=f'Category_{k}')
            category.save()
        for i in range(1, count + 1):
            _author = AuthorModel(name=f'Author_{i}',
                                  surname=f'Surname_{i}',
                                  email=f'mail{i}@mail.ru',
                                  biography=f'Biography_{i}',
                                  birthday=datetime.now())
            author.save()
            for j in range(1, count + 1):
                _category = CategoryModel.objects.filter(pk=j).first()
                article = ArticleModel(
                    title=f'Title-{j}',
                    content=" ".join(random.choices(text, k=64)),
                    date_of_publication=datetime.now(),
                    author=_author,
                    category=_category,
                    number_of_views=random.randint(1, 1000),
                    published=random.choice([True, False])
                )
                article.save()
