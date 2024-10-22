from django.shortcuts import render, redirect
import tradingeconomics as te
from django.conf import settings
from django.urls import reverse
import requests
import json

API_KEY = settings.API_KEY
te.login(API_KEY)

def index(request):
    countries = json.dumps(['mexico', 'sweden', 'new zealand', 'Thailand' ])
    data = ""
    # no access for free user
    # data = te.getForecastData(country=countries)
    return render(request, 'home/index.html', context={'data': data, 'countries': countries})

def country(request):
    
    countries = te.getAllCountries()
    return render(request, 'home/country.html', context={'countries': countries})

def indicators(request, country):
    
    try:
        indicators = te.getIndicatorData(country=country)
        return render(request, 'home/indicator.html', context={'indicators': indicators})
    except:
        return render(request, 'home/error.html')
    
def markets(request):
    xmarkets = te.getMarketsSearch(country='New Zealand')
    markets = [x for x in xmarkets if len(x['Symbol']) > 0]
    return render(request, 'home/markets.html', context={'markets': markets})

def calendar(request):
    
    try:
        calendars = te.getCalendarData()
        return render(request, 'home/calendar.html', context={'calendars': calendars})
    except:
        return render(request, 'home/error.html')
    
def news(request):
    try:
        xnews = te.getNews()
        news = [x for x in xnews if len(x['id']) > 0]
        return render(request, 'home/news.html', context={'news': news})
    except:
        return render(request, 'home/error.html')

def search(request):
    q = request.GET.get('q','')
    if q is not None:
        url = f'https://brains.tradingeconomics.com/v2/search/wb,fred,comtrade?q={q}&pp=50&p=0&_=1557934352427&stance=2'
        data = requests.get(url).json()
        return render(request, 'home/search.html', context={'data': data})