from django.db import models
from ingredients.models import Ingredient
from django.shortcuts import reverse

difficutly_choices = (
    ('easy','Easy'),
    ('medium', 'Meduim'),
    ('intermediate', 'Intermediate'),
    ('hard', 'Hard')
)

# Create your models here.
class Recipe(models.Model):
    name= models.CharField(max_length=120)
    ingredients= models.ManyToManyField(Ingredient, related_name="recipes", through="recipe_ingredients.RecipeIngredient")
    cooking_time= models.PositiveIntegerField()
    difficulty= models.CharField(max_length=20, choices=difficutly_choices)
    directions= models.TextField(default="directions")
    pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')
    
    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse ('recipes:detail', kwargs={'pk': self.pk})
    
    def get_ingredients(self):
        return "\n".join([i.quantity + ' ' + i.ingredient.name for i in self.recipeingredient_set.all()])