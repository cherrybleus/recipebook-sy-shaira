from django.db import models
from django.urls import reverse


class Ingredient(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:recipe', args=[self.pk])


class Recipe(models.Model):
    name = models.CharField(max_length=1000)
    author = models.CharField(max_length=255)
    createdOn = models.DateTimeField(auto_now_add=True, null=True)
    updatedOn = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:recipe', args=[self.pk])


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=1000)

    ingredient = models.ForeignKey(
        'Ingredient',
        on_delete = models.CASCADE,
        related_name = 'recipe'
    )

    recipe = models.ForeignKey(
        'Recipe',
        on_delete = models.CASCADE,
        related_name = 'ingredient'
    )