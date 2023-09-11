from django.core.management.base import BaseCommand
from shopapp.models import ProductModel


class Command(BaseCommand):
    help = "Update  product name by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')
        parser.add_argument('name', type=str, help='Product name')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        product = ProductModel.objects.filter(pk=pk).first()
        product.name = name
        product.save()
        self.stdout.write(f'{product}')
