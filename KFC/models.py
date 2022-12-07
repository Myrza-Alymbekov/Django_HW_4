from django.db import models


class User(models.Model):
    username = models.CharField(max_length=40, unique=True, verbose_name='Логин')
    password = models.CharField(max_length=40, verbose_name='Пароль')

    def __str__(self):
        return self.username


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name='ФИО')
    card_number = models.CharField(max_length=16, unique=True, verbose_name='Номер карты')

    def __str__(self):
        return self.name


class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name='ФИО')
    position = models.CharField(max_length=50, verbose_name='Должность')

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование ингредиента')
    extra_price = models.IntegerField(verbose_name='Стоимость надбавки')

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование блюда')
    start_price = models.IntegerField(verbose_name='Начальная стоимость блюда')
    ingredients = models.ManyToManyField(Ingredient, related_name='food', through='Order')

    def __str__(self):
        return self.name


class Order(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, related_name='orders', on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, related_name='orders', on_delete=models.CASCADE)
    order_date_time = models.DateTimeField(verbose_name='Время заказа', auto_now_add=True)

    def __str__(self):
        return f'{self.client.name} - {self.worker.name} - {self.food.name} - {self.ingredient.name}'
