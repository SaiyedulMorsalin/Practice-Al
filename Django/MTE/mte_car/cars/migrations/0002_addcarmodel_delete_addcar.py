# Generated by Django 5.0.7 on 2024-07-11 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddCarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=250)),
                ('car_price', models.IntegerField()),
                ('car_brand', models.CharField(max_length=100)),
                ('car_make', models.CharField(max_length=100)),
                ('car_model', models.CharField(max_length=100)),
                ('car_year', models.IntegerField()),
                ('car_mileage', models.IntegerField()),
                ('car_location', models.CharField(max_length=150)),
                ('car_description', models.TextField()),
                ('car_body_style', models.CharField(max_length=150)),
                ('car_drive_type', models.CharField(max_length=150)),
                ('car_stock_id', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='AddCar',
        ),
    ]
