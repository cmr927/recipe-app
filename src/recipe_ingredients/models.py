from django.db import models
from ingredients.models import Ingredient
from recipes.models import Recipe

# Create your models here.
class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe_ingredients')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='ingredient_recipes')
    quantity = models.CharField(max_length=50) # e.g., '2 cups', '1 tbsp

    def __str__(self):
        return f"{self.quantity} of {self.ingredient.name} for {self.recipe.name}"