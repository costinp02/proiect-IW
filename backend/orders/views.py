from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer

class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)
    
order_list_create_view = OrderListCreateAPIView.as_view()


class OrderDetailAPIView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'pk'

order_detail_view = OrderDetailAPIView.as_view()


class OrderUpdateAPIView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        return super().perform_update(serializer)

order_update_view = OrderUpdateAPIView.as_view()

class OrderDestroyAPIView(generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'pk'

order_destroy_view = OrderDestroyAPIView.as_view()