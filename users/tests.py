from django.test import TestCase
from .models import User #to access User model

# Create your tests here.
class UserModelTest(TestCase):
   
   def setUpTestData():
       #Set up non-modified objects used by all test methods
       User.objects.create(name= 'masterchef', email= 'masterchef@gmail.com')
       
   def test_user_name(self):
        #Get a user object to test
        user = User.objects.get(id=1)
        
        #Get the metadata for the 'name' field and use it to query its data
        field_lable = user._meta.get_field('name').verbose_name
        
        #Compare the value to the expected result
        self.assertEqual(field_lable, 'name') 
 
   def test_name_max_length(self):
        #Get a user object to test
        user = User.objects.get(id=1)
        
        #Get the metadata for the 'name' field and use it to query its max_length
        max_length = user._meta.get_field('name').max_length
        
        #Compare the value to the expected result i.e. 120
        self.assertEqual(max_length, 120) 
        
   def test_email_max_length(self):
        #Get a user object to test
        user = User.objects.get(id=1)
        
        #Get the metadata for the 'email' field and use it to query its max_length
        max_length = user._meta.get_field('email').max_length
        
        #Compare the value to the expected result i.e. 254
        self.assertEqual(max_length, 254) 