# Generated by Django 4.2.8 on 2023-12-21 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blok', '0002_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelTable(
            name='category',
            table='category',
        ),
    ]
