from rest_framework import generics

from .models import Product
from api.mixins import PharmacistPermissionMixin
from .serializers import ProductSerializer, ProductDetailSerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_list_view = ProductListAPIView.as_view()


class ProductListCreateAPIView(
    PharmacistPermissionMixin,
    generics.ListCreateAPIView): 

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        decription = serializer.validated_data.get('description') or None
        if decription is None:
            decription = name
        serializer.save(description=decription)

product_list_create_view = ProductListCreateAPIView.as_view()


class ProductDetailAPIView(
    generics.RetrieveAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    # lookup_field = 'pk' 

product_detail_view = ProductDetailAPIView.as_view()


class ProductUpdateAPIView(
    PharmacistPermissionMixin,
    generics.UpdateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        # return super().perform_update(serializer)
        instance = serializer.save()

product_update_view = ProductUpdateAPIView.as_view()


class ProductPatchAPIView(
    PharmacistPermissionMixin,
    generics.RetrieveUpdateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

product_patch_view = ProductPatchAPIView.as_view()


class ProductDestroyAPIView(
    PharmacistPermissionMixin,
    generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

product_destroy_view = ProductDestroyAPIView.as_view()



