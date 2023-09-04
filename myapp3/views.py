from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, get_object_or_404 # get_object_or_404 работает аналогично get,т.е.делает selectз апрос к базе данных.Но если запрос не вернёт строку из таблицы БД,представление отрисует страницу с ошибкой 404.
from django.views.generic import TemplateView  # позволяет создавать представления на основе класса
from.models import Author, Post


def hello(request):   # request серым цветом, мы ничего не принимаем, но для джанго это обязательная переменная
    return HttpResponse("Hello World from function!")


class HelloView(View):
    def get(self, request):                    # get или post запросы
        return HttpResponse("Hello World from class!")


def year_post(request, year):  # принимает обьект запроса и год
    text = ""
    ... # формируем статьи за год
    return HttpResponse(f"Posts from {year}<br>{text}")


class MonthPost(View):
    def get(self, request, year, month):
        text = ""
        ... # формируем статьи загод и месяц
        return HttpResponse(f"Posts from {month}/{year}<br>{text}")


def post_detail(request, year, month, slug):
    ... # Формируем статьи за год и месяц по идентификатору. Пока обойдёмся без запросов к базе данных
    post = {
        "year": year,
        "month": month,
        "slug": slug,
        "title": "Кто быстрее создаёт списки в Python,list()или []",
        "content": "В процессе написания очередной программы задумался над тем, какой способ создания списков в Python работаетбыстрее..."
    }
    return JsonResponse(post, json_dumps_params={'ensure_ascii': False}) # возвращаем список пост в джейсон обьект json_dumps_params={'ensure_ascii': False} это кодировка русского языка


def my_view(request):
    context = {"name": "John"}  # словарь где ключ совпадает с переменной внутри шаблона {{name}}
    return render(request, "myapp3/my_template.html", context) # request - пришел запрос от пользователя и возвращаем ему текст с шаблоном


class TemplIf(TemplateView):
    template_name = "myapp3/templ_if.html"   # имя переменной имя шаблона

    def get_context_data(self, **kwargs):   # распаковка словаря - ключа и значения любой набор пар
        context = super().get_context_data(**kwargs) # super() обращаемся к родительскому классу и извелкаем его данные (**kwargs) + добавляем свои данные
        context['message'] = "Привет,мир!"
        context['number'] = 5
        return context


def view_for(request):
    my_list = ['apple', 'banana', 'orange']
    my_dict = {
        'каждый': 'красный',
        'охотник': 'оранжевый',
        'желает': 'жёлтый',
        'знать': 'зелёный',
        'где': 'голубой',
        'сидит': 'синий',
        'фазан': 'фиолетовый',
    }
    context = {'my_list': my_list, 'my_dict': my_dict} # ключи должны иметь те имена которые мы используем внутри шаблона, а значения должны совпадать с именами переменных внутри представления в templ_for html так и написано my_list и my_dict
    return render(request, 'myapp3/templ_for.html', context) # принимает запрос пользователя отправляет в шаблон и пробрасывает туда текст


def index(request):
    return render(request, "myapp3/index.html") #  возвращаем шаблон index


def about(request):
    return render(request, "myapp3/about.html") #  возвращаем шаблон about


def author_posts(request, author_id): # получаем ответ от пользователя и id автора
    author = get_object_or_404(Author, pk=author_id) # извлекаем автора, либо вернет нам автора либо ошибку 404
    posts = Post.objects.filter(author=author).order_by('-id')[:5] # если нашли автора, то находим все посты, которые написал автор order_by('-id') отсортирует нам стать по id в обратном порядке [:5] и возьми 5 записей с начала
    return render(request, 'myapp3/author_posts.html', {'author': author, 'posts': posts})


def post_full(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'myapp3/post_full.html', {'post': post}) # с помощью функции рендер отрисовываем шаблон post_full передавая туда в качестве контекста этот самый post по ключу пост