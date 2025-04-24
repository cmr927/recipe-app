from django.db import models

# Create your models here.
class About(models.Model):
    name= models.CharField(max_length=120)
    bio= models.TextField()
    # Not sure where to upload_to and not sure if I want a picture. 
    # pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')
    
    def __str__(self):
        return str(self.name)
    
    
