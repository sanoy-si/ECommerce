# Generated by Django 4.2.5 on 2023-09-16 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_cart_cartitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='postal_code',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
