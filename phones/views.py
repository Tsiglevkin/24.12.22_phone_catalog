from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    """Пустой запрос делает редирект на каталог"""
    return redirect('catalog')


def show_catalog(request):
    """Обработчик сортирует данные по стоимости и имени. если нет сортировки, выводит базовый порядок"""
    template = 'catalog.html'
    sorting = request.GET.get('sort')
    if sorting == 'name':
        phones = Phone.objects.order_by(sorting)  # order_by сортирует по заданному полю.
    elif sorting == 'min_price':
        phones = Phone.objects.order_by('-price')  # '-' сортирует от минимума
    elif sorting == 'max_price':
        phones = Phone.objects.order_by('price')
    else:
        phones = Phone.objects.all()

    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    """Функция показывает информацию телефона по конкретному slug'у."""
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {
        'phone': phone
    }
    return render(request, template, context)
