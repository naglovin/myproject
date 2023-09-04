from django.urls import path
from .views import hello, HelloView, year_post, MonthPost, post_detail, my_view, TemplIf, view_for, index, about
from .views import author_posts, post_full

urlpatterns = [
    path('hello/', hello, name='hello'),  # путь по адресу 'hello/' вызывает представление hello и доп имя для представления name='hello'
    path('hello2/', HelloView.as_view(), name='hello2'), # HelloView.as_view() тут передаем класс с методом as.view()
    path('posts/<int:year>/', year_post, name='year_post'),# <int:year> т.е в переменную я хочу получить целое число полученные данные передаю в year_post и указываю имя name='year_post'
    path('posts/<int:year>/<int:month>/', MonthPost.as_view(), name='month_post'), # если между слешами будет два числа, то первое я интерпретирую как год, второе как месяц. Если совпало то вызывается представление на основе класса MonthPost.as_view()
    path('posts/<int:year>/<int:month>/<slug:slug>/', post_detail,name='post_detail'), # имя команды и ее переменной куда мы ее помещаем <slug:slug>
    path('', my_view, name='index'),                                      # '' базовый адрес
    path('if/', TemplIf.as_view(), name='templ_if'),
    path('for/', view_for, name='templ_for'),
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('author/<int:author_id>/', author_posts, name='author_posts'), # если пользователь введет author а после <int:author_id> то сработает представление author_posts которое вернет ему 5 статей
    path('post/<int:post_id>/', post_full, name='post_full'),

]