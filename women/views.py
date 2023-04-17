from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index(request): #HttpRequest
    return HttpResponse("Страница приложения women.")


def categories(request, catid):
    if request.GET:
        print(request.GET)

    return HttpResponse(f"<h1>Статья по категориям</h1><p>{catid}</p>")


def archive(request, year):
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def pageNotFound(request, *args, **kwargs):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")