from django.db import models
from users.models import User
NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(max_length=100, verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(max_length=100, verbose_name='Описание', **NULLABLE)
    image = models.ImageField(verbose_name='Изображение', upload_to='img/', **NULLABLE)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='Цена', **NULLABLE)
    data_created = models.DateTimeField(verbose_name='Дата последнего изменения', auto_now_add=True)
    vers = models.ForeignKey('Version', verbose_name='Версия', on_delete=models.DO_NOTHING, **NULLABLE)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Contacts(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    phone = models.CharField(max_length=15, verbose_name='Телефон')
    message = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return f"{self.name}({self.phone})"

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Version(models.Model):
    prod = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.CASCADE)
    number_version = models.PositiveIntegerField(verbose_name='Номер версии')
    name_version = models.CharField(max_length=100, verbose_name='Имя версии')
    current_version = models.BooleanField(verbose_name='Текущая версия', default=False)

    def __str__(self):
        return f"{self.prod.name} - {self.name_version}"

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
