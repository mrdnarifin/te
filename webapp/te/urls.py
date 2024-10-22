"""
URL configuration for te project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import country, indicators, markets, calendar,news, search, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('country/', country, name="country"),
    path('<str:country>', indicators, name="indicators"),
    path('markets/', markets, name="markets"),
    path('calendar/', calendar, name="calendar"),
    path('news/', news, name="news"),
    path('search/', search, name="search"),
]
