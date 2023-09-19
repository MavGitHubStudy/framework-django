from django.db import models
from django.db.models import Manager
from django.urls import reverse


class CustomerModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    registration = models.DateTimeField()

    objects = Manager()

    def __str__(self):
        return (f'{self.name} {self.email} {self.phone} {self.address} '
                f'{self.registration}')

    class Meta:
        ordering = ['-registration']


def get_absolute_url():
    # return reverse('cls_article', kwargs={'pk': self.pk})
    return reverse('products')


class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.IntegerField()
    added = models.DateTimeField()
    image = models.ImageField(upload_to='images/', blank=True)

    objects = Manager()

    def __str__(self):
        return (f'{self.name} {self.description} {self.price} {self.quantity} '
                f'{self.added}')

    class Meta:
        ordering = ['-added']

    @staticmethod
    def return_all_products():
        return ProductModel.objects.all()


class OrderModel(models.Model):
    customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE)
    products = models.ManyToManyField(ProductModel, through="OrderDetailsModel")
    total_price = models.DecimalField(decimal_places=2, max_digits=10)
    placed = models.DateTimeField()

    objects = Manager()

    def __str__(self):
        return f'{self.customer}'

    class Meta:
        ordering = ['-placed']


class OrderDetailsModel(models.Model):
    ordermodel_id = models.ForeignKey(OrderModel, on_delete=models.CASCADE)
    producmodel_id = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity_in_order = models.IntegerField()
