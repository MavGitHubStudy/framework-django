from django.core.management.base import BaseCommand
from shopapp.models import CustomerModel


class Command(BaseCommand):
    help = "Get last n  customers."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='count last customers')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        customers = CustomerModel.objects.all()[:count]
        self.stdout.write(f'{customers}')
