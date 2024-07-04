from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PostModel(models.Model):
    title = models.CharField(max_length=150)
    post_content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    CHOICE_LIST = [
        ('M', 'Medium'),
        ('S', 'Small'),
        ('L', 'Large')
    ]
    category = models.CharField(max_length=1, choices=CHOICE_LIST)

    def __str__(self):
        return self.title
