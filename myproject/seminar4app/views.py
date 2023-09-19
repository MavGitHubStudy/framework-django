from django.shortcuts import render

from django.http import HttpResponse

from .forms import ChooseGameForm
# без нижеуказанного импорта возникает ошибка !
from .utils import HeadsOrTails, Dice, RandomNumber

from seminar4app.models import AuthorModel, ArticleModel
from django.views.generic import CreateView, DetailView, TemplateView
from .forms import AddAuthorForm
from .forms import AddArticleForm


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
    # success_url = reverse_lazy('seminar4app:author_page')


class AuthorPage(DetailView):
    model = AuthorModel
    template_name = 'seminar4app/author_page.html'


class AllArticlesView(TemplateView):
    template_name = "seminar4app/articles.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = AuthorModel.objects.get(pk=self.kwargs['id_author'])
        articles = ArticleModel.objects.filter(author=author).all()
        context['articles'] = articles
        context['realization'] = 'class representation'
        return context


class DetailArticle(DetailView):
    model = ArticleModel
    template_name = "seminar4app/detail_article.html"
    context_object_name = 'article'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.number_of_views += 1
        obj.save()
        return obj



class AddArticle(CreateView):
    model = ArticleModel
    template_name = 'seminar4app/add_article.html'
    form_class = AddArticleForm
