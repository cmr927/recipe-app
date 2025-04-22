from django.db import models

class User(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return str(self.name)


