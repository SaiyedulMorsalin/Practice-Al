from django.contrib import admin
from .models import LoginModel,SignUpModel
# Register your models here.
admin.site.register(LoginModel)
admin.site.register(SignUpModel)