from django.db import models
from recipes.models import Recipe #because we need to connect home with recipes. Modeled off of "sales" from lesson.

# Create your models here.
class Home(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    price = models.FloatField()
    date_created=models.DateTimeField(blank=True)
    
    def __str__(self):
        return f"id: {self.id}, recipe: {self.recipe.name}, quantity: {self.quantity}"

