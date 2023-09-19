from random import randint

from django.http import HttpResponse
from django.shortcuts import render

# from seminar2app.models import GameModel
from .models import GameModel, AuthorModel, CategoryModel, ArticleModel


def single_game(request):
    result = ('TAILS', 'HEAD')[randint(0, 1)]

    game = GameModel(result=result)
    game.save()

    return HttpResponse(f'{game}')


def last_games(request):
    last = GameModel().return_last(5)
    last_str = ['<br>' + str(i) for i in last]

    return HttpResponse(last_str)


def last_authors(request):
    all_authors = AuthorModel().return_all_authors()
    all_authors_str = ['<br>' + str(i) for i in all_authors]

    return HttpResponse(all_authors_str)


def all_categories(request):
    _all_categories = CategoryModel().return_all_categories()
    _all_categories_str = ['<br>' + str(i) for i in _all_categories]

    return HttpResponse(_all_categories_str)


def last_articles(request):
    last = ArticleModel().return_last_articles(5)
    last_str = ['<br>' + str(i) for i in last]

    return HttpResponse(last_str)
