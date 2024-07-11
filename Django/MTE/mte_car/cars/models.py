from django.db import models

# Create your models here.
class AddCarModel(models.Model):
    car_image1 = models.ImageField(upload_to="cars_images/",blank=True,null=True)
    car_image2 = models.ImageField(upload_to="cars_images/",blank=True,null=True)
    car_image3 = models.ImageField(upload_to="cars_images/",blank=True,null=True)
    car_name = models.CharField(max_length=250)
    car_type = models.CharField(max_length=100,blank=True,null=True)
    car_price = models.IntegerField()
    car_brand = models.CharField(max_length=100)
    car_make = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    car_year = models.IntegerField()
    car_mileage = models.IntegerField()
    car_location = models.CharField(max_length=150)
    car_description = models.TextField()
    car_body_style = models.CharField(max_length=150)
    car_drive_type = models.CharField(max_length=150)
    car_stock_id = models.IntegerField()
    
    def __str__(self):
        return self.car_name
class CommentModel(models.Model):
    car = models.OneToOneField(AddCarModel,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique= True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comments by {self.name}"