from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk')
    class Meta:
        model = Product
        fields = [
            'url',
            'id',
            'name',
            'price',
            'weight',
            'type',
            'description',
            'stock',
            'expiry_date',

        ]

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'price',
            'weight',
            'type',
            'description',
            'stock',
            'expiry_date',
        ]