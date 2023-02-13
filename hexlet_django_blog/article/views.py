from django.shortcuts import render

def article(request, tags, article_id):
    return render(request, 'article.html', context={
        'article': f'Статья номер {article_id}. Тег {tags}',
    })
