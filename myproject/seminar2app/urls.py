from django.urls import path
from seminar2app import views


app_name = 'seminar2app'

urlpatterns = [
    path('single_game/', views.single_game, name='single_game'),
    path('last_games/', views.last_games, name='last_games'),
    path('last_authors/', views.last_authors, name='last_authors'),
    path('all_categories/', views.all_categories, name='all_categories'),
]
