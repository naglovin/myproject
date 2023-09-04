from django.core.management.base import BaseCommand
from myapp2.models import Author, Post


class Command(BaseCommand):
    help = "Get all posts by author id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='UserID') # получаем наш первичный ключ из консоли


    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')            # извлекаем этот ключ из командной строки
        author = Author.objects.filter(pk=pk).first() # извлекаем одного автора
        if author is not None:
            posts = Post.objects.filter(author=author)  # извлекаем все посты автора
            intro = f'All posts of {author.name}\n'
            text = '\n'.join(post.content for post in posts) # собираем все посты воедино
            self.stdout.write(f' {intro} {text}')
