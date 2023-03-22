from rest_framework import generics
from .models import Address
from .serializers import AddressSerializer, AddressDetailSerializer

    #list items and can also create new items (combines create and list)
class AddressListCreateAPIView(generics.ListCreateAPIView): 
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)
    
    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     request = self.request
    #     print(request.user)
    #     if request.user.is_superuser:
    #         print("YO")
    #         return super().get_queryset(*args, **kwargs)
    #     print("SUP")
    #     return qs.filter(client=request.user)
    
address_list_create_view = AddressListCreateAPIView.as_view()


class AddressDetailAPIView(generics.RetrieveAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressDetailSerializer
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


class AddressPatchAPIView(generics.RetrieveUpdateAPIView):

    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    lookup_field = 'pk'

address_patch_view = AddressPatchAPIView.as_view()


class AddressDestroyAPIView(generics.DestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    lookup_field = 'pk'

address_destroy_view = AddressDestroyAPIView.as_view()

