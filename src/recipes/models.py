from django.db import models
from ingredients.models import Ingredient
from django.shortcuts import reverse

# Create your models here.
class Recipe(models.Model):
    name= models.CharField(max_length=120)
    ingredients= models.ManyToManyField(Ingredient, related_name="recipes", through="recipe_ingredients.RecipeIngredient")
    cooking_time= models.PositiveIntegerField()
    difficulty= models.CharField(max_length=20)
    directions= models.TextField(default="directions")
    pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')
    
    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse ('recipes:detail', kwargs={'pk': self.pk})
    
    def get_ingredients(self):
        '''
        Param: self
        Displays the quantities and ingredients next to each other
        '''  
        return "\n".join([i.quantity + ' ' + i.ingredient.name for i in self.recipeingredient_set.all()])
    
    def calc_difficulty (self):
        '''
        Param: self
        Calculates the difficulty level of recipe. Retuns the difficulty of the recipe.
        '''  
        if self.cooking_time < 10 and len(self.recipeingredient_set.all()) < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and len(self.recipeingredient_set.all()) >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and len(self.recipeingredient_set.all()) < 4:
            self.difficulty = "Intermediate"
        elif self.cooking_time >= 10 and len(self.recipeingredient_set.all()) >= 4:
            self.difficulty = "Hard"           
        return self.difficulty