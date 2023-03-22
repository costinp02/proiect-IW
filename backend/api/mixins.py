from rest_framework import permissions

from .permissions import IsPharmacistPermission

class PharmacistPermissionMixin():
    permission_classes = [permissions.IsAdminUser, IsPharmacistPermission]