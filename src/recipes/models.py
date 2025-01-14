from django.db import models

difficutly_choices = (
    ('easy','Easy'),
    ('medium', 'Meduim'),
    ('intermediate', 'Intermediate'),
    ('hard', 'Hard')
)

# Create your models here.
class Recipe(models.Model):
    name= models.CharField(max_length=120)
    ingredients= models.TextField(default="no ingredients yet")
    cooking_time= models.PositiveIntegerField()
    difficulty= models.CharField(max_length=20, choices=difficutly_choices)
    
    def __str__(self):
        return str(self.name)
