from django.db import models
from django.contrib.auth.models import AbstractUser #, BaseUserManager
# from django.db.models.signals import post_save
# from django.dispatch import receiver

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        CLIENT = "CLIENT", 'Client'
        PHARMACIST = "PHARMACIST", 'Pharmacist'

    base_role = Role.CLIENT

    role = models.CharField(max_length=50,choices=Role.choices, default=Role.CLIENT)
    cnp = models.CharField(max_length=13,null=True, blank=True) #can be none for pharmacist, admin

