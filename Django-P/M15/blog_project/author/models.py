from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=300)
    phone_number = models.CharField(max_length=11)
    
    def __str__(self):
        return f"{self.name}"