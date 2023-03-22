from rest_framework import serializers

from .models import Address
from users.serializers import UserSerializer

class AddressSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='address-detail', lookup_field='pk')
    # client = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Address
        fields = [
            'url',
            'client',
            'id',
            'address_info',
            'postal_code',
            'city',
        ]

class AddressDetailSerializer(serializers.ModelSerializer):
    client = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Address
        fields = [
            'client',
            'id',
            'address_info',
            'postal_code',
            'city',
        ]