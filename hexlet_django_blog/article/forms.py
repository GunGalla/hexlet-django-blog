from django import forms
from django.forms import ModelForm

from .models import Article

class CommentArticleForm(forms.Form):
    content = forms.CharField(label='Комментарий')


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'body']

