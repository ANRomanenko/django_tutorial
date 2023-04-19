from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


def index(request): #HttpRequest
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})


def about(request): #HttpRequest
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О нас'})


def categories(request, catid):
    if request.GET:
        print(request.GET)

    return HttpResponse(f"<h1>Статья по категориям</h1><p>{catid}</p>")


def archive(request, year):
    if int(year) > 2020:
        return redirect('/', permanent=True) # Таким способом можно делать редирект 302 и 301
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def pageNotFound(request, *args, **kwargs):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")