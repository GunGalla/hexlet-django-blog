from django.shortcuts import render, get_object_or_404
from django.views import View

from hexlet_django_blog.article.models import Article


class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'index_art.html', context={
            'articles': articles,
        })


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'show.html', context={
            'article': article,
        })
