from django.shortcuts import render
from django.db.models import Sum

from myapp5.models import Product



def total_in_db(request):
    total = Product.objects.aggregate(Sum('quantity')) # сумма по столбцу количество aggregate - метод запроса к базе данных
    context = {
        'title': 'Общее количество посчитано в базеданных',
        'total': total,
    }
    return render(request, 'myapp6/total_count.html', context) # myapp6/total_count.htm универсальный шаблон для трех представлений


def total_in_view(request):
    products = Product.objects.all()                 # помещаем абсолютно все продукты
    total = sum(product.quantity for product in products)  # перебераю каждый продкт, обращаюсь к его свойству quantity и суммурую его
    context = {
        'title': 'Общее количество посчитано в представлении',
        'total': total,
    }
    return render(request, 'myapp6/total_count.html', context)


def total_in_template(request):  # будет работать напрямую с классом продукт
    context = {
        'title': 'Общее количество посчитано в шаблоне',
        'products': Product,
    }
    return render(request, 'myapp6/total_count.html', context)
