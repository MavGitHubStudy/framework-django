from django.urls import path
from .views import index


app_name = 'seminar5app'

urlpatterns = [
    path('index/', index, name='sem5_index'),
]
