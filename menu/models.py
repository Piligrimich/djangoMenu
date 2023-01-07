from django.db import models


class Menu(models.Model):
    title = models.CharField('Название меню', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, blank=True, on_delete=models.CASCADE, verbose_name='Название меню')
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, verbose_name='Родительский элемент')
    title = models.CharField(verbose_name='Название пункта', max_length=255)
    slug = models.SlugField(max_length=255, unique=True, verbose_name='slug')

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self):
        return self.title
