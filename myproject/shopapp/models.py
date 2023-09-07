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

    objects = Manager()

    def __str__(self):
        return f'{self.name} {self.description} {self.price} {self.quantity} {self.added}'

    class Meta:
        ordering = ['-added']


class OrderModel(models.Model):
    customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE)
    products = models.ManyToManyField(ProductModel)
    total_price = models.DecimalField(decimal_places=2, max_digits=10)
    placed = models.DateTimeField(auto_now_add=True)

    objects = Manager()

    def __str__(self):
        return f'{self.customer} {self.products} {self.total_price} {self.placed}'

    class Meta:
        ordering = ['-placed']

    # Уточнить работы с такой моделью!
