from random import choices                        # выбор случайным образом каки е то значения
from django.core.management.base import BaseCommand # для создания команд
from myapp3.models import Author, Post


# LOREM набор случайного текста

LOREM = "Lorem ipsum dolor sit amet, consectetur adipisicing elit."\
        "Accusamus accusantium aut beatae consequatur consequunturcumque,delectusetilloistemaxime"\
        "nihilnonnostrumodioofficia,perferendisplaceat quasiquibusdamquisquamquodsunt"\
        "tempore temporibus ut voluptatum? A aliquam culpa ducimus,eaqueeumillomollitianemo"\
        "tempore unde vero! Blanditiis deleniti ex hic, laboriosammaioresoditofficiapraesentium"\
        "quaequisquamratione,reiciendis,veniam.Accusantium assumendaconsecteturconsequatur"\
        "consequunturcorporisdignissimosducimuseiusesteum expeditailloin,inventore"\
        "ipsumiustomaioresminusmollitianecessitatibusneque nisioptioquasiquoquod,"\
        "quosremrepellendustemporibustotamundevelvelit verovitaevoluptates."


class Command(BaseCommand):
    help = "Generate fake authors and posts."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='UserID')  # принимаем count как ключ словаря

    def handle(self, *args, **kwargs):
        text = LOREM.split()     # делим весь текст на отдельные слова
        count = kwargs.get('count')# извлекаем то число которое мы передали в командной строке
        for i in range(1, count + 1):
            author = Author(name=f'Author_{i}', email=f'mail{i}@mail.ru') # пробегаем от 1 до count включительно +1 добавляем цифру и сохраняем
            author.save()
            for j in range(1, count + 1):   # c постами делаем точно так же как и с авторами
                post = Post(
                    title=f'Title-{j}',    # какой то заголовок
                    content=" ".join(choices(text, k=64)), # рандомно возьми 64 слова и сформируй из этого строку текста разделенный пробелом
                    author=author  # в качестве автора указываем модель в 27 строке
                )
                post.save()