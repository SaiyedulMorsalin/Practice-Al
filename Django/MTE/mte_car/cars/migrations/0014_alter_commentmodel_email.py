# Generated by Django 5.0.7 on 2024-07-11 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0013_alter_addcarmodel_car_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodel',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]