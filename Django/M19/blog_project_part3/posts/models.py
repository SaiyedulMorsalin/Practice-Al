from django.db import models
from categories.models import Category
from django.contrib.auth.models import User
# Create your models here.
class PostModel(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title