from django.core.management.base import BaseCommand
from shopapp.models import OrderModel, CustomerModel, ProductModel


class Command(BaseCommand):
    help = "Create  order."

    def handle(self, *args, **kwargs):
        order = CustomerModel(name='Mary', email='mary@example.com', phone='+7(977)333-33-33',
                                 address="Mary's address")
        customer.save()
        self.stdout.write(f'{customer}')
