from random import choice, randint, uniform
from django.core.management.base import BaseCommand
from myapp5.models import Category, Product


class Command(BaseCommand):
    help = "Generate fake products."

    def add_arguments(self, parser):
        """В методе add_arguments()определяется аргумент командной строки'count', который будет содержать количество продуктов, которые нужно сгенерировать."""
        parser.add_argument('count', type=int, help='UserID')

    def handle(self, *args, **kwargs):
        """Метод handle() вызывается при выполнении команды.Он получает все категории из БД, создает список продуктов и заполняет его фейковыми данными
        Затем,используя метод bulk_create(),продукты сохраняются вБД."""
        categories = Category.objects.all()  # запрос к базе данных, выбираем все категории
        products = []   # список продуктов которые мы захртим добвить
        count = kwargs.get('count')    # число продктов которое нам надо сгенерировать
        for i in range(1, count + 1):  #
            products.append(Product(        # в список продуктов добавляем очередной продукт
                name=f'продукт номер{i}',
                category=choice(categories),  # случайный выбор категорий из общего числа категорий
                description='длинное описание продукта,которое и так никто не читает',
                price=uniform(0.01, 999_999.99),
                quantity=randint(1, 10_000),
                rating=uniform(0.01, 9.99),
            ))
        Product.objects.bulk_create(products)  # bulk_create принимает список обьектов и добавляем в базу данных
