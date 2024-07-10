from django.db import models
from categories.models import Category
from django.contrib.auth.models import User
# Create your models here.
class PostModel(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='./posts/media/',blank=True,null=True)
    
    def __str__(self):
        return self.title
    
    

class CommentModel(models.Model):
    post = models.ForeignKey(PostModel,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) #jokhni ei class er object toiri hbe sei time ta rekhe dibe
    def __str__(self):
        return f"Comments by {self.name}"