from django.urls import path
from .views import *


app_name = 'menu'


urlpatterns = [
    path('', main, name='main'),
    path('<slug:slug>', menu_item_view, name='menu_item'),
]
