import random
import feedparser
from django.core.cache import cache
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpRequest

def home_url(request):
    context = {

    }
    return render(request, 'myapp/home.html', context=context)

def about(request):
    context = {

    }
    return render(request, 'myapp/about.html', context=context)


def home_view(request):
    latest_news = cache.get('external_news')
    if not latest_news:
        # Если в кэше пусто, делаем запрос к чужому сайту
        rss_url = "https://positivnews.ru/category/zhivotnye/"
        try:
            feed = feedparser.parse(rss_url)
            latest_news = feed.entries[:3]
            # Сохраняем результат в кэш на 15 минут (900 секунд)
            cache.set('external_news', latest_news, 900)
        except Exception:
            latest_news = []

    return render(request, 'myapp/home.html', {'news_list': latest_news})



