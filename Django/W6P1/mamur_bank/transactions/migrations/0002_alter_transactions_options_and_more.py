# Generated by Django 5.0.7 on 2024-07-26 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transactions',
            options={'ordering': ['timestamp']},
        ),
        migrations.AlterField(
            model_name='transactions',
            name='transaction_type',
            field=models.IntegerField(choices=[(1, 'Deposit'), (2, 'Withdrawal'), (3, 'Loan'), (4, 'Loan Paid')], null=True),
        ),
    ]