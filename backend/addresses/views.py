from rest_framework import generics
from .models import Address
from .serializers import AddressSerializer

    #list items and can also create new items (combines create and list)
class AddressListCreateAPIView(generics.ListCreateAPIView): 
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)
    
address_list_create_view = AddressListCreateAPIView.as_view()

class AddressDetailAPIView(generics.RetrieveAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    lookup_field = 'pk'

address_detail_view = AddressDetailAPIView.as_view()

class AddressUpdateAPIView(generics.UpdateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        # return super().perform_update(serializer)
        instance = serializer.save()

address_update_view = AddressUpdateAPIView.as_view()

class AddressDestroyAPIView(generics.DestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    lookup_field = 'pk'

address_destroy_view = AddressDestroyAPIView.as_view()

