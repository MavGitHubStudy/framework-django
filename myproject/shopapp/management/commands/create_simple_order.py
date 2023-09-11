from django.core.management.base import BaseCommand
from shopapp.models import OrderModel, CustomerModel, ProductModel, OrderItemModel


class Command(BaseCommand):
    help = "Create  simple order."

    def handle(self, *args, **kwargs):
        customer = CustomerModel.objects.filter(pk=1).first()
        product = ProductModel.objects.filter(pk=1).first()

        # order = OrderModel(customer_id=customer,
        #                    total_price=product.get_price())
        # order.save()

        # order_item = OrderItemModel(order=order,
        #                             product=product,
        #                             item_quantity=1)
        # order_item.save()

