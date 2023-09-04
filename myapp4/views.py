import logging

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from.forms import UserForm, ManyFieldsForm, ManyFieldsFormWidget
from.models import User
from.forms import ImageForm


logger = logging.getLogger(__name__)
def user_form(request):

    """Далее определяем функцию user_form,которая будет обрабатывать запросы на адрес/user_form/.
    Если запрос пришел методом POST,то мы создаем экземпля рформы UserFormс переданными данными из запроса.Если форма проходит валидацию(всеполя заполненыкорректно),
    то мы получаем данные из формы и можем с ними работать.
    Если запрос пришел методом GET,то мы просто создаем пустой экземпляр формы UserForm и передаем его в шаблон user_form.html."""
    if request.method == 'POST':   # проверка пост или гет запрос
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']   # cleaned_data это данные которые прошли валидацию
            age = form.cleaned_data['age'] #Делаемчто-тосданными
            logger.info(f'Получили {name=}, {email=}, {age=}.')
    else:
        form = UserForm()
    return render(request, 'myapp4/user_form.html', {'form': form})


def many_fields_form(request):
    if request.method == 'POST':   # проверка пост или гет запрос
        form = ManyFieldsFormWidget(request.POST)
        if form.is_valid():
            logger.info(f'Получили {form.cleaned_data=}.')
    else:
        form = ManyFieldsFormWidget()
    return render(request, 'myapp4/many_fields_form.html', {'form': form})


# def many_fields_form(request):
#     if request.method == 'POST':   # проверка пост или гет запрос
#         form = ManyFieldsForm(request.POST)
#         if form.is_valid():
#             logger.info(f'Получили {form.cleaned_data=}.')
#     else:
#         form = ManyFieldsForm()
#     return render(request, 'myapp4/many_fields_form.html', {'form': form})


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            logger.info(f'Получили{name=},{email=},{age=}.')
            user = User(name=name, email=email, age=age)
            user.save()
            message = 'Пользователь сохранён'
    else:
        form = UserForm()
        message = 'Заполните форму'
    return render(request, 'myapp4/user_form.html', {'form': form, 'message': message})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES) # request.POST чтобы получить текстовую информацию , request.FILES чтобы получить байты
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()  # FileSystemStorage экземпляр позволяет работать с файлами
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'myapp4/upload_image.html', {'form': form})
