# Generated by Django 5.0.6 on 2024-07-30 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_useraddress_postal_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbankaccount',
            name='bankrupt',
            field=models.BooleanField(default=False),
        ),
    ]
