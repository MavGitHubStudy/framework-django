from django.core.management.base import BaseCommand
from shopapp.models import CustomerModel


class Command(BaseCommand):
    help = "Get customer by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Customer ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        customer = CustomerModel.objects.filter(pk=pk).first()
        self.stdout.write(f'{customer}')
