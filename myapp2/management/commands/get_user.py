from django.core.management.base import BaseCommand
from myapp2.models import User


# class Command(BaseCommand):
#     help = "Get user byid."
#
#     def add_arguments(self, parser):
#         parser.add_argument('id', type=int, help='UserID') # принимает парсер с id числовым и подсказкой что это id пользователя
#
#     def handle(self, *args, **kwargs):
#         id = kwargs['id']                  # из словаря кваргс по имени айди извлекаем значение целого типа
#         user = User.objects.get(id=id)     # и методом get найди нам тот самый id. Если такого пользователя нет get выведет ошибку. лучше использовать filter
#         self.stdout.write(f'{user}')


class Command(BaseCommand):
    help = "Get user by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='UserID') # тот же код что и выше, pk первичный ключ вместо id чтобы не ругалась программа

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        user = User.objects.filter(pk=pk).first()      # фильтр вместо get не выведет ошибок если такого персонажа нет first() - покажет первого если их несколько
        self.stdout.write(f'{user}')
