from django.test import TestCase
from .models import Ingredient #to access Ingredient model

# Create your tests here.
class IngredientModelTest(TestCase):
   
   def setUpTestData():
       #Set up non-modified objects used by all test methods
       Ingredient.objects.create(name='salt')
       
   def test_ingredient_name(self):
        #Get an ingredient object to test
        ingredient = Ingredient.objects.get(id=1)
        
        #Get the metadata for the 'name' field and use it to query its data
        field_lable = ingredient._meta.get_field('name').verbose_name
        
        #Compare the value to the expected result
        self.assertEqual(field_lable, 'name') 
 
   def test_name_max_length(self):
        #Get an ingredient object to test
        ingredient = Ingredient.objects.get(id=1)
        
        #Get the metadata for the 'name' field and use it to query its max_length
        max_length = ingredient._meta.get_field('name').max_length
        
        #Compare the value to the expected result i.e. 100
        self.assertEqual(max_length, 100) 

