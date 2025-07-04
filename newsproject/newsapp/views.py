from django.shortcuts import render, get_object_or_404
from .models import News, Category
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

def home(request):
    news_list = fetch_real_news()
    return render(request, 'newsapp/home.html', {'news_list': news_list})

def news_detail(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    return render(request, 'newsapp/detail.html', {'news': news})

def fetch_real_news():
    print("Loaded API KEY:", os.getenv('NEWSAPI_KEY'))  # Debug line
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'language': 'en',
        'apiKey': os.getenv('NEWSAPI_KEY')
    }
    response = requests.get(url, params=params)
    data = response.json()
    if data.get('status') == 'ok':
        return data.get('articles', [])
    else:
        print('API error:', data)
        return []
