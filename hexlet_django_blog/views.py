from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse

class Index(View):
    
    def get(self, request, *args, **kwargs):
        return redirect(reverse('article', kwargs={'tags': 'python', 'article_id': 42}))


def about(request):
    tags = ['обучение', 'программирование', 'python', 'oop']
    return render(request, 'about.html', context={'tags': tags})
