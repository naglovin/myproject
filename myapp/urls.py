from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),  # импортируем индекс из модуля вью и даем имя индекс '' -ЭТО ПУСТАЯ СТРОКА, Т,Е начальная страница
    path('about/', views.about, name='about'),]  # по пути about/ импортируем эбаут из модуля вью и даем имя эбаут)