from django.core.management.base import BaseCommand
from shopapp.models import ProductModel


class Command(BaseCommand):
    help = "Get all  products."

    def handle(self, *args, **kwargs):
        products = ProductModel.objects.all()
        self.stdout.write(f'{products}')
