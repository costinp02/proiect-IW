from django.db import models
from products.models import Product
from users.models import User

class Order(models.Model):
    class StatusTypes(models.TextChoices):
        PENDING = "PENDING", 'Order status is pending'
        ACCEPTED = "ACCEPTED", 'Order has been accepted'
        REJECTED = "REJECTED", 'Order has been rejected'

    base_status = StatusTypes.PENDING

    client_id = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=StatusTypes.choices, default=base_status)
    products = models.ManyToManyField(Product)


