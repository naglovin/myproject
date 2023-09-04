"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # include подключение к маршрутам проекта, маршрут приложения
from myapp3.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prefix/', include('myapp.urls')),  # по пути пустой строки 127.0.0.1 8000 подключаем модуль myapp. myapp.urls создаем в myapp
    path('les3/', include('myapp3.urls')), # для пути les3/ я хочу подключить include из каталога myapp3 файл urls.
    # Если пользователь заходит в les3/ то основной urls понимает что нужно передать управление в myapp3.urls чтобы определить какая view будет работать
    path('', index),  # будет базовой страничкой моего сайта
    path('les4/', include('myapp4.urls')),
    #path('__debug__/', include("debug_toolbar.urls")), # отключае при развертывании проекта, пользователь не должен видеть отладку
    path('les6/',include('myapp6.urls')),
]
