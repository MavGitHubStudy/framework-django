from datetime import datetime

from django import forms
from django.forms import ModelForm


# import myshopapp.models
from myshopapp.models import ProductModel


class ProductForm(ModelForm):
    added = forms.DateField(initial=datetime.today,
                            widget=forms.DateInput(
                                attrs={'class': 'form-control', 'type': 'date'}))

    class Meta:
        # Название модели на основе которой создаётся форма
        model = ProductModel
        # Включаем все поля из модели в форму
        fields = '__all__'
