from django.db import models
from django.db.models import Manager
from django.urls import reverse


# from django.contrib.auth.models import User


class GameModel(models.Model):
    result = models.CharField(max_length=10)
    played = models.DateTimeField(auto_now_add=True)

    objects = Manager()

    def __str__(self):
        return f'Объект Результата игры: {self.result}, время: {self.played}'

    def single_game(self):
        return f'Результат игры: {self.result}'

    class Meta:
        ordering = ['-played']

    @staticmethod
    def return_last(n):
        return GameModel.objects.all()[:n]


class AuthorModel(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField(max_length=1000)
    birthday = models.DateField()

    objects = Manager()

    def get_absolute_url(self):
        return reverse('seminar2app:author_page', kwargs={'pk': self.pk})

    def __str__(self):
        return (f'{self.name} {self.surname} {self.email} {self.biography} '
                f'{self.birthday}')

    def full_name(self):
        return f'{self.name} {self.surname}'

    @staticmethod
    def return_all_authors():
        return AuthorModel.objects.all()


class CategoryModel(models.Model):
    name = models.CharField(max_length=100)

    objects = Manager()

    def __str__(self):
        return f'{self.name}'

    @staticmethod
    def return_all_categories():
        return CategoryModel.objects.all()


class ArticleModel(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_of_publication = models.DateField(auto_now_add=True)
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryModel, on_delete=models.DO_NOTHING)
    number_of_views = models.IntegerField(default=0)
    published = models.BooleanField(default=False)

    objects = Manager()

    def get_absolute_url(self):
        return reverse('cls_article', kwargs={'pk': self.pk})

    def __str__(self):
        return (f'{self.title} {self.content} {self.date_of_publication} '
                f'{self.author} {self.category} {self.number_of_views} '
                f'{self.published}')

    class Meta:
        ordering = ['-date_of_publication']

    @staticmethod
    def return_last_articles(n):
        return ArticleModel.objects.all()[:n]


class CustomerModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    register_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.email} {self.address} {self.phone}"


class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.IntegerField()
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product_name} {self.price} {self.amount}"


class OrderModel(models.Model):
    customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE)
    products = models.ManyToManyField(ProductModel)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"{self.customer} {self.products} {self.total_price} "
                f"{self.order_date}")
