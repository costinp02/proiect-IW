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

    role = models.CharField(max_length=50,choices=Role.choices, default=base_role)
    cnp = models.CharField(max_length=13,null=True, blank=True) #can be none for pharmacist, admin











#Client model extension

# class ClientManager(BaseUserManager):
#     def get_queryset(self, *args, **kwargs):
#         results = super().get_queryset(*args, **kwargs)
#         return results.filter(role=User.Role.CLIENT)

# class Client(User):
#     base_role = User.Role.CLIENT

#     client = ClientManager()

#     class Meta:
#         proxy = True

# @receiver(post_save, sender=Client)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created and instance.role == "CLIENT":
#         ClientProfile.objects.create(user=instance)

# class ClientProfile(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     cnp = models.CharField(max_length=10)


