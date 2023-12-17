from django.db import models

# Create your models here.
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    text = models.TextField(null=True , blank=True , verbose_name='Описание')
    created_add = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')
    update_add = models.DateTimeField(auto_now=True , verbose_name='Дата обновления')


    def __str__(self) -> str:
        return f'{self.title} {self.text}'


    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'