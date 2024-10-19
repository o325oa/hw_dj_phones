from django.shortcuts import render, redirect, get_object_or_404
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_order = request.GET.get('sort',
                                 'name')  # Получаем параметр сортировки из GET-запроса
    if sort_order == 'min_price':
        phones = Phone.objects.all().order_by('price')  # Сортировка по цене (по возрастанию)

    elif sort_order == 'max_price':
        phones = Phone.objects.all().order_by('-price')  # Сортировка по цене (по убыванию)
    elif sort_order == 'name':
        phones = Phone.objects.all().order_by('name')  # Сортировка по названию (по возрастанию)
    else:
        phones = Phone.objects.all().order_by('name')  # По умолчанию сортировка по названию
    context = {
        'phones': phones,
        'sort_order': sort_order
    }
    return render(request, template, context)

def show_product(request, slug):
    template = 'product.html'
    phone = get_object_or_404(Phone, slug=slug)
    context = {
        'phone': phone
    }
    return render(request, template, context)

