# Generated by Django 5.0.7 on 2024-07-11 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_addcarmodel_delete_addcar'),
    ]

    operations = [
        migrations.AddField(
            model_name='addcarmodel',
            name='car_image1',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='addcarmodel',
            name='car_image2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='addcarmodel',
            name='car_image3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]