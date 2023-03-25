from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product
from products.serializers import ProductSerializer

@api_view(['GET'])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    print("Not Valid")
    return None
    # instance = Product.objects.all().first()
    # data = {}
    # if instance:
    #     data = ProductSerializer(instance).data
    # return Response(data)