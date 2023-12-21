from django.db import models

# Create your models here.
from django.db import models




class BaseModel(models.Model):
    created_add = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')
    update_add = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        abstract = True

class Product(BaseModel):
    image = models.ImageField(upload_to='posts',null=True,blank=False,verbose_name='Фото')
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    text = models.TextField(null=True , blank=True , verbose_name='Описание')
    rate = models.FloatField(default=0 , verbose_name='Рейтинг')

    def __str__(self) -> str:
        return f'{self.title} {self.text} '


    class Meta:
        db_table = 'product'
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Category(BaseModel):
    post = models.ForeignKey(
        'blok.Product',
        on_delete=models.CASCADE ,
        verbose_name='пост',
        related_name='Категория')
    text = models.CharField(max_length=200,verbose_name='Категория')

    def __str__(self) -> str:
        return f'{self.text}'
    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'