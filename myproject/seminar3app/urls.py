from django.urls import path
from .views import main, about_me
from .views import MainView, AboutMeView
from .views import HeadsGame, DiceGame
from .views import AllArticlesView, DetailArticle

urlpatterns = [
    path('main/', main, name='main'),
    path('about_me/', about_me, name='about_me'),
    path('cls_main/', MainView.as_view(), name='cls_main'),
    path('cls_about_me/', AboutMeView.as_view(), name='cls_about_me'),
    path('cls_heads_game/<int:count>/', HeadsGame.as_view(), name='cls_heads'),
    path('cls_dice_game/<int:count>/', DiceGame.as_view(), name='cls_dice'),
    path('cls_articles/<int:id_author>', AllArticlesView.as_view(),
         name='cls_articles'),
    path('cls_article/<int:pk>', DetailArticle.as_view(), name='cls_article')
]
