from django.core.management.base import BaseCommand
from shopapp.models import CustomerModel


class Command(BaseCommand):
    help = "Create  customer."

    def handle(self, *args, **kwargs):

        # customer = CustomerModel(name='John', email='john@example.com', phone='+7(916)111-11-11',
        #                          address="John's address")
        # customer = CustomerModel(name='Tom', email='tom@example.com', phone='+7(905)222-22-22',
        #                          address="Tom's address")
        customer = CustomerModel(name='Mary', email='mary@example.com', phone='+7(977)333-33-33',
                                 address="Mary's address")
        customer.save()
        self.stdout.write(f'{customer}')
