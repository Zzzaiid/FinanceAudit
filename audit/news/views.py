from django.shortcuts import render
from .models import Article

def news(request):
    news = Article.objects.all()
    return render(request, 'news/news.html', {'news': news})