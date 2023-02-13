from django.shortcuts import render
from django.views import View

class Index(View):
    
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', context={
            'who': 'World',
        })


def about(request):
    tags = ['обучение', 'программирование', 'python', 'oop']
    return render(request, 'about.html', context={'tags': tags})
