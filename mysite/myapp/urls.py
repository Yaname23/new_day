from django.contrib import admin
from django.urls import path
from .views import home_url, about

app_name = 'myapp'

urlpatterns = [

    path("", home_url, name='home'),
    path('about/', about, name='about'),
]