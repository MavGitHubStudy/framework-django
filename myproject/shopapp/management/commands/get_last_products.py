from django.core.management.base import BaseCommand
from shopapp.models import ProductModel


class Command(BaseCommand):
    help = "Get last n  products."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='count last products')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        products = ProductModel.objects.all()[:count]
        self.stdout.write(f'{products}')
