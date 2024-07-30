# Generated by Django 5.0.7 on 2024-07-27 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_alter_transactions_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='transaction_type',
            field=models.IntegerField(choices=[(1, 'Deposit'), (2, 'Withdraw'), (3, 'Loan'), (4, 'Loan Paid')], null=True),
        ),
    ]
