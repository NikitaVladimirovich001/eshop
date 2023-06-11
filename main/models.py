from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=15, verbose_name='Название')
    def __str__ (self):
        return self.name
    class Meta:
        ordering = ('name',)

class Product(models.Model):
    name = models.CharField(max_length=15, verbose_name='Название')
    manufacturer = models.ForeignKey('Manufacturer',on_delete=models.CASCADE, verbose_name='Производитель')
    garanty = models.PositiveIntegerField(verbose_name='Гарянтия')
    count = models.PositiveIntegerField(verbose_name='Количество')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    class Meta:
        ordering = ('name',)

class Country(models.Model):
    name = models.CharField(max_length=15,verbose_name='Название')

class Manufacturer(models.Model):
    name = models.CharField(max_length=15,verbose_name='Название')
    addres = models.CharField(max_length=50,verbose_name='Адрес')
    phone_number = models.PositiveIntegerField(verbose_name='Номер телефона')
    def __str__ (self):
        return self.name




