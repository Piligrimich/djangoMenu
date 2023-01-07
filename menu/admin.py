from django.contrib import admin
from .models import *


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')
    list_filter = ('menu',)
    fieldsets = (
        ('Добавить элемент меню', {
            'description': "Родителем может быть само меню или элемент меню",
            'fields': (('menu', 'parent'), 'title', 'slug')
            }),
            )
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title',)
