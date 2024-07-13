from django.db import models
from brands.models import BrandModel
from django.contrib.auth.models import User
# Create your models here.
class CarModel(models.Model):
    car_image1 = models.ImageField(upload_to="cars_images/",blank=True,null=True)
    car_image2 = models.ImageField(upload_to="cars_images/",blank=True,null=True)
    car_image3 = models.ImageField(upload_to="cars_images/",blank=True,null=True)
    car_name = models.CharField(max_length=250)
    CAR_TYPE =[
        ('New','New'),
        ('Used','Used')
    ]
    car_type = models.CharField(max_length=5,choices=CAR_TYPE,blank=True,null=True)
    car_price = models.IntegerField()
    car_stock = models.IntegerField(blank=True,null=True)
    car_brand = models.ForeignKey(BrandModel,on_delete=models.CASCADE,blank=True,null=True)
    car_make = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    car_year = models.IntegerField()
    car_mileage = models.IntegerField()
    car_location = models.CharField(max_length=150)
    car_description = models.TextField()
    car_body_style = models.CharField(max_length=150)
    car_drive_type = models.CharField(max_length=150)
    car_stock_id = models.IntegerField()
    car_vin = models.CharField(max_length=100,blank=True,null=True)
    STATUS_LIST =[
        ('In Stock','In Stock'),
        ('Out Of Stock','Out Of Stock')
    ]
    car_status = models.CharField(max_length=30,choices=STATUS_LIST,blank=True,null=True)
    car_users = models.ManyToManyField(User,related_name='cars')
    
    
    def __str__(self):
        return self.car_name
class CommentModel(models.Model):
    car = models.ForeignKey(CarModel,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comments by {self.name}"
    
    


    