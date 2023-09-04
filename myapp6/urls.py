from django.urls import path
from .views import total_in_db, total_in_view, total_in_template  # импорт трех представлений

urlpatterns = [
    path('db/', total_in_db, name='db'),     # общая сумма из баззы данных
    path('view/', total_in_view, name='view'),    # через представление
    path('template/', total_in_template, name='template'), # через шаблон
]
