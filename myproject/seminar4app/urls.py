from django.urls import path
from .views import game_play, authors, AddAuthor, AuthorPage
from .views import AllArticlesView, DetailArticle, AddArticle

app_name = 'seminar4app'

urlpatterns = [
    path('game/', game_play, name='game_play'),
    path('authors/', authors, name='authors'),
    path('add_author/', AddAuthor.as_view(), name='add_author'),
    path('author_page/<int:pk>', AuthorPage.as_view(), name='author_page'),
    path('cls_articles/<int:id_author>', AllArticlesView.as_view(),
         name='cls_articles'),
    path('cls_article/<int:pk>', DetailArticle.as_view(), name='cls_article'),
    path('article/add', AddArticle.as_view(), name='add_article'),
]
