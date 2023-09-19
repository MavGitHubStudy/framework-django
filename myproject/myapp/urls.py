from django.urls import path
from .views import index, about

urlpatterns = [
    # path('index/', index, name='index'),
    path('', index, name='index'),
    path('about/', about, name='about'),
]
