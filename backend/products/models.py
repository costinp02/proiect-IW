from django.db import models
from datetime import date
# Create your models here.
class Product(models.Model):
    CAPSULES = 'CA'
    DROPS = 'DR'
    POWDER ='PO'
    LIQUID = 'LI'
    TABLETS = 'TA'
    OTHER = 'OT'

    MED_TYPE = [
        (CAPSULES, 'Capsules'),
        (DROPS, 'Drops'),
        (POWDER, 'Powder'),
        (LIQUID, 'Liquid'),
        (TABLETS, 'Tablets'),
        (OTHER, 'Other')

    ]


    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    weight = models.DecimalField(max_digits=10,decimal_places=2, default=0.00)
    type = models.CharField(max_length=50, choices=MED_TYPE,default=OTHER)
    description = models.TextField(blank=True,null=True)
    stock = models.DecimalField(max_digits=4,decimal_places=0)
    expiry_date = models.DateField(default=date.today)
