from django.test import TestCase
from .models import RecipeIngredient
from ingredients.models import Ingredient
from recipes.models import Recipe

# Create your tests here.
class RecipeIngredientModelTest(TestCase):
    
    def setUpTestData():
        #Set up non-modified objects used by all test methods
        recipe = Recipe.objects.create(name= 'Peanut Butter Sandwich', cooking_time= 5, difficulty='Easy')
        ingredient_1 = Ingredient.objects.create(name= 'Peanut Butter')
        ingredient_2 = Ingredient.objects.create(name='Bread')
        ingredient_recipe_1 = RecipeIngredient.objects.create(ingredient=ingredient_1, recipe= recipe, quantity="2oz")
        ingredient_recipe_2 = RecipeIngredient.objects.create(ingredient=ingredient_2, recipe= recipe, quantity="2 slices")
       
        recipe.ingredients.add(ingredient_1)
        recipe.ingredients.add(ingredient_2)
        
    def test_recipe_name(self):
        #Get a recipe_ingredient object to test
        recipe_ingredient = RecipeIngredient.objects.get(id=1)
        
        # Extracting the ingredient from the recipe_ingredient object
        recipe = recipe_ingredient.recipe
         
        #Compare the value to the expected result
        self.assertEqual(recipe.name, 'Peanut Butter Sandwich')    
    
    def test_recipe_ingredient_ingredient(self):
        #Get a recipe_ingredient object to test
        recipe_ingredient = RecipeIngredient.objects.get(id=1)
        
        # Extracting the ingredient from the recipe_ingredient object
        ingredient = recipe_ingredient.ingredient
         
        #Compare the value to the expected result
        self.assertEqual(ingredient.name, 'Peanut Butter')
        
    def test_recipe_ingredient_quantity(self):
        #Get a recipe_ingredient object to test
        recipe_ingredient = RecipeIngredient.objects.get(id=1)
        
        quantity = recipe_ingredient.quantity
         
        #Compare the value to the expected result
        self.assertEqual(quantity, '2oz')
 
    def test_quantity_max_length(self):
        #Get an ingredient object to test
        ingredient = RecipeIngredient.objects.get(id=1)
        
        #Get the metadata for the 'quantity' field and use it to query its max_length
        max_length = ingredient._meta.get_field('quantity').max_length
        
        #Compare the value to the expected result i.e. 50
        self.assertEqual(max_length, 50)     
