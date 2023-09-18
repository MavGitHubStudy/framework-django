from django.shortcuts import render

from django.http import HttpResponse
from django.urls import reverse_lazy

from .forms import ChooseGameForm

# без этого импорта возникает ошибка !
from .utils import HeadsOrTails, Dice, RandomNumber

# модель берём из семинара 4
from seminar4app.models import AuthorModel, ArticleModel
# from seminar4app.models import CategoryModel

from django.views.generic import CreateView, DetailView
from .forms import AddAuthorForm, AddArticleForm


def game_play(request):
    results = []
    if request.method == 'POST':
        form = ChooseGameForm(request.POST)
        if form.is_valid():
            selected_game = form.cleaned_data['game']
            # нижеуказанная строка вызовет ошибку,
            # если закомментировать строку № 3 !!!
            game = globals()[selected_game]()
            attempts = form.cleaned_data['count']
            for i in range(attempts):
                game.play()
                results.append(str(game))
    else:
        form = ChooseGameForm()
    return render(request, 'seminar4app/game.html',
                  {'form': form, 'results': results})


def authors(request):
    all_authors = AuthorModel().return_all_authors()
    all_authors_str = ['<br>' + str(i) for i in all_authors]

    return HttpResponse(all_authors_str)


class AddAuthor(CreateView):
    model = AuthorModel
    template_name = 'seminar4app/add_author.html'
    form_class = AddAuthorForm


class AuthorPage(DetailView):
    model = AuthorModel
    template_name = 'seminar4app/author_page.html'


class AddArticle(CreateView):
    model = ArticleModel
    template_name = 'seminar4app/add_article.html'
    form_class = AddArticleForm
