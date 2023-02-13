from django.db import models

class Article(models.Model):
    name = models.CharField(max_length=200) # название статьи
    body = models.TextField() # тело статьи
    timestamp = models.DateTimeField(auto_now_add=True)
# Create your models here.
