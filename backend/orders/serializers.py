from rest_framework import serializers

from .models import Order
from products.serializers import ProductSerializer

class OrderSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="order-detail", lookup_field='pk')
    class Meta: 
        model = Order
        fields = [
            'url',
            'id',
            'client_id',
            'status',
            'products'
            
        ]


class OrderDetailSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    class Meta: 
        model = Order
        fields = [
            'id',
            'client_id',
            'status',
            'products',
            
        ]

