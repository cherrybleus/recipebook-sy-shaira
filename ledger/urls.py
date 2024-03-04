from django.urls import path

from .views import RecipeDetailView, RecipesListView

urlpatterns = [
    path('recipes/list', RecipesListView.as_view(), name='list'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe'),
]

app_name = 'ledger'