from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]


def index(request): #HttpRequest
    posts = Women.objects.filter(is_published=True)
    cats = Category.objects.all()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=context)


def about(request): #HttpRequest
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О нас'})


def addpage(request):
    return HttpResponse("Обратная связь")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def pageNotFound(request, *args, **kwargs):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def show_post(request, post_id):
    return HttpResponse(f"Отображение стати с id = {post_id}")


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context=context)


# def categories(request, catid):
#     if request.GET:
#         print(request.GET)
#
#     return HttpResponse(f"<h1>Статья по категориям</h1><p>{catid}</p>")
#
#
# def archive(request, year):
#     if int(year) > 2020:
#         return redirect('/', permanent=True) # Таким способом можно делать редирект 302 и 301
#     return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")
