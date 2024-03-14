from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe

class RecipesListView(ListView):
    model = Recipe
    template_name = 'recipes.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe.html'