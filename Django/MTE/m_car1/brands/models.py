from django.db import models

# Create your models here.
class BrandModel(models.Model):
    brand_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True)
    brand_image = models.ImageField(upload_to="brands_image_logo/",blank=True,null=True)
    
    
    def __str__(self):
        return self.brand_name