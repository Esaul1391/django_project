from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Главная страница')


def group_posts(request):
    return HttpResponse('Список')


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
# def ice_cream_detail(request, pk):
#     return HttpResponse(f'Мороженое номер {pk}')