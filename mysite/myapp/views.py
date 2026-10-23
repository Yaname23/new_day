from django.contrib.auth import logout, login, authenticate

from django.http import HttpResponse, HttpRequest
import random
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse


def home_url(request):
    context = {

    }
    return render(request, 'myapp/home.html', context=context)

def about(request):
    context = {

    }
    return render(request, 'myapp/about.html', context=context)
