# Generated by Django 5.0.7 on 2024-07-11 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0010_addcarmodel_car_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcarmodel',
            name='car_type',
            field=models.IntegerField(blank=True, choices=[('new', 'New'), ('used', 'Used')], null=True),
        ),
    ]