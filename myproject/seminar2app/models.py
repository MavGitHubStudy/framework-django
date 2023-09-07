from django.db import models
from django.db.models import Manager


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

    def __str__(self):
        return f'{self.name} {self.surname} {self.email} {self.biography} {self.birthday}'

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

    def __str__(self):
        return (f'{self.title} {self.content} {self.date_of_publication} '
                f'{self.author} {self.category} {self.number_of_views} '
                f'{self.published}')

    class Meta:
        ordering = ['-date_of_publication']

    @staticmethod
    def return_last_articles(n):
        return ArticleModel.objects.all()[:n]
