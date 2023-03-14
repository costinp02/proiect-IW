import json
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().first()
    data = {}
    if model_data:
        data = model_to_dict(model_data)
    return Response(data)