from django.urls import path
from .views import game_play, authors, AddAuthor, AuthorPage
# from seminar2app.views import authors

app_name = 'seminar4app'

urlpatterns = [
    path('game/', game_play, name='game_play'),
    path('authors/', authors, name='authors'),
    path('add_author/', AddAuthor.as_view(), name='add_author'),
    path('author_page/<int:pk>', AuthorPage.as_view(), name='author_page'),
]
