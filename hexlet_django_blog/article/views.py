from django.shortcuts import render
from django.views import View

from hexlet_django_blog.article.models import Article


class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'index_art.html', context={
            'articles': articles,
        })


def article(request, tags, article_id):
    return render(request, 'article.html', context={
        'article': f'Статья номер {article_id}. Тег {tags}',
    })
