from django.core.management.base import BaseCommand
from shopapp.models import ProductModel


class Command(BaseCommand):
    help = "Create  product."

    def handle(self, *args, **kwargs):

        # product = ProductModel(name='Product1', description='Description1', price=1000.50, quantity=50)
        # product = ProductModel(name='Product2', description='Description2', price=3000.85, quantity=30)
        product = ProductModel(name='Product3', description='Description3', price=1500.00, quantity=40)

        product.save()
        self.stdout.write(f'{product}')
