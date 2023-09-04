from django.db import models


class User(models.Model):     # наследуемся от класса model
    name = models.CharField(max_length=100)        # Создаем столбцы таблицы, id в django проставится автоматически
    email = models.EmailField()
    password = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return f'User name: {self.name}, email:{self.email}, age: {self.age}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2) # максимум чисел 8 и мест после запятой 2
    description = models.TextField()                            # какой то очень большой текст
    image = models.ImageField(upload_to='products/')            # изображение будут храниться в этом каталоге


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE) # заказчик, ссылка на пользователя и при удалении пользователя, мы удалим все его заказы
    products = models.ManyToManyField(Product)                   # много заказов могут содержать данный продукт и много продуктов могут быть в заказе
    date_ordered = models.DateTimeField(auto_now_add=True)       # при заказе автоматически ставится дата и время
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

# Создаем еще две таблицы
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'Name: {self.name}, email: {self.email}'


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE) # ссылаемся на класс автор выше, и при удалении автора удаляем все его посты

    def __str__(self):
        return f'Title is {self.title}'