# Generated by Django 3.2.12 on 2025-02-10 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_buy_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='buy',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
