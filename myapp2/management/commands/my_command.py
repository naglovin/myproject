from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Print 'Hello world!'to output." #Переменная help выведет справку по работе команды.А метод handle отработает при вызове команды в консоли.
    def handle(self, *args, **kwargs): # принимает ключевые и позиционные моменты
        self.stdout.write('Hello world!') # stdout.write стандартный вывод и напиши( то что в скобках) как принт
"""В место привычного print необходимо использовать self.stdout.write для печати информации в стандартный поток вывода-консоль."""