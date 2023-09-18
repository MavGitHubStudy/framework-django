from django.core.management.base import BaseCommand
from shopapp.models import CustomerModel


class Command(BaseCommand):
    help = "Get all  customers."

    def handle(self, *args, **kwargs):
        customers = CustomerModel.objects.all()
        self.stdout.write(f'{customers}')
