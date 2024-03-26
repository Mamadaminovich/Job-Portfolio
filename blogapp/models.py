from django.db import models

# Create your models here.
class User1(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name