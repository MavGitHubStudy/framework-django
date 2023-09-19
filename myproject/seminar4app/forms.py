from datetime import datetime
from django import forms
from seminar4app.models import AuthorModel, ArticleModel


class ChooseGameForm(forms.Form):
    GAME_CHOICES = (
        ('HeadsOrTails', 'Heads or Tails'),
        ('Dice', 'Dice'),
        ('RandomNumber', 'Random Number'),
    )

    game = forms.ChoiceField(choices=GAME_CHOICES)
    count = forms.IntegerField(min_value=1, max_value=64)


class AddAuthorForm(forms.ModelForm):
    birthday = forms.DateField(initial=datetime.today(),
                               widget=forms.DateTimeInput(
                                   attrs={'class': 'form-control',
                                          'type': 'date'}))

    class Meta:
        model = AuthorModel
        # name, surname, email, biography, birthday
        fields = ['name', 'surname', 'email', 'biography', 'birthday']


class AddArticleForm(forms.ModelForm):
    class Meta:
        model = ArticleModel
        fields = [
            'title',
            'content',
            'date_of_publication',
            'author',
            'category',
            'number_of_views',
            'published'
        ]
