from django.db import models
from users.models import User

class Address(models.Model):
    client_id = models.ForeignKey(User, on_delete=models.CASCADE)
    address_info = models.CharField(max_length=120)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=50)