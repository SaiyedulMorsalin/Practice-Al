# Generated by Django 5.0.7 on 2024-07-13 06:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0001_initial'),
        ('cars', '0017_addcarmodel_car_stock_userorder'),
        ('orders', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AddCarModel',
            new_name='CarModel',
        ),
        migrations.DeleteModel(
            name='UserOrder',
        ),
    ]
