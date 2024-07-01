from django.db import models

# Create your models here.
class PostModel(models.Model):
    post_title = models.CharField(max_length=150)
    post_content = models.TextField()
    CHOICE_LIST = {('H','Horror'),('P','Programming'),('JS','JavaScript'),('J','Java'),('C++','C++'),('C','C')}
    category = models.CharField(max_length=50,choices=CHOICE_LIST)
    
    def __str__(self):
        return self.post_title
    
    