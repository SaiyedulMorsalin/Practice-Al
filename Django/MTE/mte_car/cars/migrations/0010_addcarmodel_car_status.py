# Generated by Django 5.0.7 on 2024-07-11 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0009_addcarmodel_car_vin'),
    ]

    operations = [
        migrations.AddField(
            model_name='addcarmodel',
            name='car_status',
            field=models.ImageField(blank=True, choices=[('stock', 'In Stock'), ('out', 'Out Of Stock')], null=True, upload_to=''),
        ),
    ]