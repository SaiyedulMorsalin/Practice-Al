from django.db import models
from categories.models import Category
from author.models import Author
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ManyToManyField(Category) # ekta post multiple category er mddhe thakte pare abr ekta categorir mddhe multiple post thakte pare
    author = models.ForeignKey(Author, on_delete=models.CASCADE) # jdi amra ekjn author ke delete kri tahle tar sokol post delete hye jabe.
    
    def __str__(self):
        return f"{self.title} -- {self.author}"