from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)  # уникальная категория unique=True

    def __str__(self):
        return self.name


class Product(models.Model):
    """Модель Product содержит два поля: name,которое является строковым именем продукта,и category,которое является внешним ключом на модель Category.
    Внешний ключ определяется с помощью поля ForeignKey,которое указывает на модель Category и использует on_delete=models.CASCADE,
    чтобы обеспечить каскадное удаление,когда категория удаляется."""
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(default='', blank=True)  # default='' по умолчанию пусто, blank=True не обязательное поле
    price = models.DecimalField(default=999999.99, max_digits=8, decimal_places=2)
    quantity = models.PositiveSmallIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(default=5.0, max_digits=3, decimal_places=2)

    def __str__(self):
        return self.name

    @property  # данный декоратор говорит что данный метод, воспринимается именно как метод, а не свойство
    def total_quantity(self):
        return sum(product.quantity for product in Product.objects.all()) # перебераю каждый продкт, обращаюсь к его свойству quantity и суммурую его
