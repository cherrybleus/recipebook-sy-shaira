from django.urls import path

from .views import index, recipes, recipe_1, recipe_2

urlpatterns = [
    path('', index, name='index'),
    path('recipes/list', recipes, name='list'),
    path('recipe/1', recipe_1, name='1'),
    path('recipe/2', recipe_2, name='2')
]

app_name = 'ledger'