from django.test import TestCase
from django.urls import reverse
from .models import Recipe, Ingredient
from recipe_ingredients.models import RecipeIngredient
from .forms import RecipesSearchForm
from django.test.client import RequestFactory
from django.contrib.auth.models import AnonymousUser, User
from .views import RecipeListView, RecipeDetailView, recipe_user_input_view
from django.core.files import temp as tempfile

# Create your tests here.
class RecipeModelTest(TestCase):
   def setUpTestData():
      #Set up non-modified objects used by all test methods
      recipe = Recipe.objects.create(name= 'Peanut Butter & Jelly Sandwich', cooking_time= 5, difficulty='Easy', directions="make the sandwich")
      ingredient_1 = Ingredient.objects.create(name= 'Peanut Butter')
      ingredient_2 = Ingredient.objects.create(name= 'Jelly')
      ingredient_3 = Ingredient.objects.create(name='Bread')
      ingredient_recipe_1 = RecipeIngredient.objects.create(ingredient=ingredient_1, recipe= recipe, quantity="2oz")
      ingredient_recipe_2 = RecipeIngredient.objects.create(ingredient=ingredient_2, recipe= recipe, quantity="1oz")
      ingredient_recipe_3 = RecipeIngredient.objects.create(ingredient=ingredient_3, recipe= recipe, quantity="2 slices")
       
      recipe.ingredients.add(ingredient_1)
      recipe.ingredients.add(ingredient_2)
      recipe.ingredients.add(ingredient_3)
   
   def test_recipe_ingredients(self):
      #Testing the recipe has the correct number of ingredients
      recipe = Recipe.objects.get(id=1)
        
      self.assertEqual(len(recipe.ingredients.all()), 3)
        
   def test_get_ingredients(self):
      #Testing if the the quantities and ingredients are next to each other
      recipe = Recipe.objects.get(id=1)
      ingredients= recipe.get_ingredients()
      self.assertEqual(ingredients, '2oz Peanut Butter\n1oz Jelly\n2 slices Bread')
             
            
   def test_recipe_name(self):
      #Get a recipe object to test
      recipe = Recipe.objects.get(id=1)
        
      #Get the metadata for the 'name' field and use it to query its data
      field_lable = recipe._meta.get_field('name').verbose_name
        
      #Compare the value to the expected result
      self.assertEqual(field_lable, 'name') 
        
   def test_recipe_cooking_time(self):
      #Get a recipe object to test
      recipe = Recipe.objects.get(id=1)
        
      #Get the metadata for the 'cooking_time' field and use it to query its data
      field_lable = recipe._meta.get_field('cooking_time').verbose_name
        
      #Compare the value to the expected result
      self.assertEqual(field_lable, 'cooking time')
        
   def test_recipe_directions(self):
      #Get a recipe object to test
      recipe = Recipe.objects.get(id=1)
        
      #Get the metadata for the 'directions' field and use it to query its data
      field_lable = recipe._meta.get_field('directions').verbose_name
        
      #Compare the value to the expected result
      self.assertEqual(field_lable, 'directions')        
 
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
   
   def test_get_absolute_url(self):
      recipe = Recipe.objects.get(id=1)
      #get_absolute_url() should take you to the detail page of recipe #1
      #and load the URL /recipes/list/1
      self.assertEqual(recipe.get_absolute_url(), '/recipes/list/1')  
     
   def test_calc_difficulty_easy(self): 
      # Testing if the Easy difficulty level is calculated
      recipe = Recipe.objects.get(id=1)
      recipe.difficulty=""
      self.assertEqual(recipe.difficulty, "")
      recipe.calc_difficulty()
      self.assertEqual(recipe.difficulty, 'Easy')
          
   def test_calc_difficulty_medium(self): 
      # Testing if the Medium difficulty level is calculated
      recipe = Recipe.objects.get(id=1)
      recipe.difficulty=""
      recipe.cooking_time=5
      ingredient_4 = Ingredient.objects.create(name='Banana')
      recipe.ingredients.add(ingredient_4)
      recipe.calc_difficulty()
      self.assertEqual(recipe.difficulty, 'Medium')
          
   def test_calc_difficulty_intermediate(self): 
      # Testing if the Intermediate difficulty level is calculated
      recipe = Recipe.objects.get(id=1)
      recipe.difficulty=""
      recipe.cooking_time=10
      recipe.calc_difficulty()
      self.assertEqual(recipe.difficulty, 'Intermediate')     
          
   def test_calc_difficulty_hard(self): 
      # Testing if the Hard difficulty level is calculated
      recipe = Recipe.objects.get(id=1)
      recipe.difficulty=""
      recipe.cooking_time=10
      ingredient_4 = Ingredient.objects.create(name='Banana')
      recipe.ingredients.add(ingredient_4)
      recipe.calc_difficulty()
      self.assertEqual(recipe.difficulty, 'Hard')   
          
class RecipeFormTest(TestCase):       
   def test_recipe_form(self):
      form_data = {'recipe_title': 'soup', 'ingredient_title': 'broth', 'chart_type': '#1'}
      form = RecipesSearchForm(data=form_data)
      self.assertTrue(form.is_valid())
      
   def test_recipe_form_invalid_chart(self):
      form_data = {'recipe_title': 'soup', 'ingredient_title': 'broth', 'chart_type': '#4'}
      form = RecipesSearchForm(data=form_data)
      self.assertFalse(form.is_valid())
      
   def test_recipe_form_invalid_recipe_title(self):
      form_data = {'recipe_title': 'sooooooooooooooooooooooooooooooooooooooooooooooooooooupsooooooooooooooooooooooooooooooooooooooooooooooooooooupsooooooooooooooooooooooooooooooooooooooooooooooooooooup', 'ingredient_title': 'broth', 'chart_type': '#1'}
      form = RecipesSearchForm(data=form_data)
      self.assertFalse(form.is_valid())
      
   def test_recipe_form_invalid_ingredient_title(self):
      form_data = {'recipe_title': 'soup', 'ingredient_title': 'broooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooth', 'chart_type': '#1'}
      form = RecipesSearchForm(data=form_data)
      self.assertFalse(form.is_valid())
        
   def test_recipe_form_missing_ingredient_title(self):
      form_data = {'recipe_title': 'soup', 'ingredient_title': '', 'chart_type': '#1'}
      form = RecipesSearchForm(data=form_data)
      self.assertTrue(form.is_valid())
      
   def test_recipe_form_missing_recipe_title(self):
      form_data = {'recipe_title': '', 'ingredient_title': 'broth', 'chart_type': '#1'}
      form = RecipesSearchForm(data=form_data)
      self.assertTrue(form.is_valid())
      
class TestRecipeListView(TestCase):
   def setUp(self):
      self.factory = RequestFactory()
      self.user = User.objects.create_user(
      username='test1',
      email='abc1@gmail.com',
      first_name='t',
      last_name='u',
      password='password'
        )
      
   def test_recipe_list_view_with_valid_user(self):
      request = self.factory.get('/recipes/list/')
      request.user = self.user
      response = RecipeListView.as_view()(request)
      self.assertEqual(response.status_code, 200)
      self.assertEqual(response.template_name[0], 'recipes/main.html')
      
   def test_recipe_list_view_with_anonymous_user(self):
      request = self.factory.get('/recipes/list/')
      request.user = AnonymousUser()
      response = RecipeListView.as_view()(request)
      self.assertEqual(response.status_code,302)

class TestRecipeUserInputView(TestCase):
   def setUp(self):  
      self.factory = RequestFactory()  
      self.user = User.objects.create_user(
      username='test1',
      email='abc1@gmail.com',
      first_name='t',
      last_name='u',
      password='password'
        )
      self.ingredient_1 = Ingredient.objects.create(name= 'Peanut Butter')
      self.ingredient_2 = Ingredient.objects.create(name= 'Jelly')
   
   def test_get_recipe_user_input_view(self):
      request = self.factory.get('/recipes/create/')
      request.user = self.user
      response = recipe_user_input_view(request)
      self.assertEqual(response.status_code, 200)
      
   def test_post_recipe_user_input_view(self):
      file = tempfile.NamedTemporaryFile()
      with open(file.name, 'rb') as test_pic:
         request = self.factory.post('/recipes/create/', {
            "name": "pb&j", 
            "ingredients": [self.ingredient_1.id, self.ingredient_2.id], 
            "cooking_time": "5", 
            "directions": "make da sandwich",
            "pic": test_pic
         }
                                  )
         request.user = self.user

         response = recipe_user_input_view(request)
      self.assertEqual(response.status_code, 200)   
      recipe = Recipe.objects.all()
      recipe_ings = RecipeIngredient.objects.all()
      self.assertEqual(len(recipe_ings), 2)
      self.assertEqual(len(recipe), 1)   
      self.assertEqual(recipe[0].name, "pb&j")   
      ingredients= recipe[0].get_ingredients()
      self.assertEqual(ingredients, '1oz Peanut Butter\n1oz Jelly')
      self.assertEqual(recipe[0].cooking_time, 5)
      self.assertEqual(recipe[0].directions, "make da sandwich")
         
        
      
      
      
      
               