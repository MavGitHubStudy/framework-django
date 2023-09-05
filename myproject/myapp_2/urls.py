from django.urls import path
from . import views

urlpatterns = [
    path('heads_or_tails/', views.heads_or_tails, name='heads_or_tails'),
    path('playing_cube_face/', views.playing_cube_face, name='playing_cube_face'),
    path('random_number/', views.random_number, name='random_number'),
]
