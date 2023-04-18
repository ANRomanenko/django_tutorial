from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index(request): #HttpRequest
    return HttpResponse("Страница приложения women.")


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