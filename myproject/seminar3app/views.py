from random import randint

from django.shortcuts import render
# from django.http import HttpResponse
# from django.views import View
from django.views.generic import TemplateView, DetailView, ListView
from .models import ArticleModel, AuthorModel
from .models import OrderModel, CustomerModel


def main(request):
    context = {"title": "Main-DjangoFramework",
               "realization": "functional representation"}
    return render(request, "seminar3app/main.html", context)


def about_me(request):
    context = {"title": "About me-DjangoFramework",
               "realization": "functional representation"}
    return render(request, "seminar3app/about_me.html", context)


class MainView(TemplateView):
    template_name = "seminar3app/main.html"

    def get_context_data(self, **kwargs):
        # Get all previous data
        context = super().get_context_data(**kwargs)
        # Create your own data
        context['title'] = 'Main-DjangoFramework'
        context['realization'] = 'class representation'
        return context


class AboutMeView(TemplateView):
    template_name = "seminar3app/about_me.html"

    def get_context_data(self, **kwargs):
        # Get all previous data
        context = super().get_context_data(**kwargs)
        # Create your own data
        context['title'] = 'About me-DjangoFramework'
        context['realization'] = 'class representation'
        return context


class GameView(TemplateView):
    template_name = "seminar3app/game.html"


class HeadsGame(GameView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        results = [
            ('TAIL', 'HEADS')[randint(0, 1)] for i in range(
                int(self.kwargs['count']))
        ]
        context['results'] = results
        context['title'] = 'Орёл или Решка-DjangoFramework'
        context['realization'] = 'class representation'
        return context


class DiceGame(GameView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        results = [
            randint(1, 6) for i in range(
                int(self.kwargs['count']))
        ]
        context['results'] = results
        context['title'] = 'Кости-DjangoFramework'
        context['realization'] = 'class representation'
        return context


# def heads(request):
#     result = ('TAIL', 'HEADS')[randint(0, 1)]
#
#     game = GameModel(result=result)
#     game.save()
#
#     return HttpResponse(f'{game}')


# def last_games(request):
#     last = GeteModel().return_last(5)
#     last_str = ['<br>' + str(i) for i in last]
#     return HttpResponse(last_str)


class AllArticlesView(TemplateView):
    template_name = "seminar3app/articles.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = AuthorModel.objects.get(pk=self.kwargs['id_author'])
        articles = ArticleModel.objects.filter(author=author).all()
        context['articles'] = articles
        context['realization'] = 'class representation'
        return context


class DetailArticle(DetailView):
    model = ArticleModel
    template_name = "seminar3app/detail_article.html"
    context_object_name = 'article'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.number_of_views += 1
        obj.save()
        return obj


class OrderProductsView(ListView):
    model = OrderModel
    template_name = '/seminar3app/order_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = CustomerModel.objects.get(pk=self.kwargs['pk'])
        orders = OrderModel.objects.filter(customer=customer).all()
        from django.db import connection
        print(connection.queries)
        context['orders'] = orders
        return context
