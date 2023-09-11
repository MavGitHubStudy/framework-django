from django.db import models
from django.db.models import Manager


class CustomerModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    registration = models.DateTimeField(auto_now_add=True)

    objects = Manager()

    def __str__(self):
        return f'{self.name} {self.email} {self.phone} {self.address} {self.registration}'

    class Meta:
        ordering = ['-registration']


class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.IntegerField()
    added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-added']

    objects = Manager()

    def __str__(self):
        return f'{self.name} {self.description} {self.price} {self.quantity} {self.added}'

    def get_price(self):
        return self.price


class OrderModel(models.Model):
    customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE)
    products = models.ManyToManyField(ProductModel)
    total_price = models.DecimalField(decimal_places=2, max_digits=10)
    placed = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-placed']

    objects = Manager()

    def __str__(self):
        return f'Order {self.pk} {self.customer}'

    # def get_total_price(self):
    #     return sum(item.get_cost() for item in self.items.all())


class OrderItemModel(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='order_items')
    item_quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.pk}'
