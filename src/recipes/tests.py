from django.test import TestCase
from .models import Recipe #to access Recipe model

# Create your tests here.
class RecipeModelTest(TestCase):
   
   def setUpTestData():
       #Set up non-modified objects used by all test methods
       Recipe.objects.create(name= 'Peanut Butter & Jelly Sandwich', ingredients= 'Peanut Butter, Jelly, Bread', cooking_time= '5', difficulty= 'medium')
       
   def test_recipe_name(self):
        #Get a recipe object to test
        recipe = Recipe.objects.get(id=1)
        
        #Get the metadata for the 'name' field and use it to query its data
        field_lable = recipe._meta.get_field('name').verbose_name
        
        #Compare the value to the expected result
        self.assertEqual(field_lable, 'name') 
 
   def test_name_max_length(self):
        #Get a recipe object to test
        recipe = Recipe.objects.get(id=1)
        
        #Get the metadata for the 'name' field and use it to query its max_length
        max_length = recipe._meta.get_field('name').max_length
        
        #Compare the value to the expected result i.e. 120
        self.assertEqual(max_length, 120) 
        
   def test_difficulty_max_length(self):
        #Get a recipe object to test
        recipe = Recipe.objects.get(id=1)
        
        #Get the metadata for the 'difficulty' field and use it to query its max_length
        max_length = recipe._meta.get_field('difficulty').max_length
        
        #Compare the value to the expected result i.e. 20
        self.assertEqual(max_length, 20) 