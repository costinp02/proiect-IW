# Generated by Django 4.1.7 on 2023-03-23 15:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='expiry_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
