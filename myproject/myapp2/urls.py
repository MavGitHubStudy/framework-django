from django.urls import path
from myapp.views import index, about

urlpatterns = [
    path('index/', index, name='index'),
    path('about/', about, name='about'),
]
