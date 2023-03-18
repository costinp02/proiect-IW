from rest_framework import generics
from .models import User
from .serializers import UserSerializer

    #creating a new user with this view will result in unencrypted password
class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)
    
user_list_create_view  = UserListCreateAPIView.as_view()

class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

user_detail_view = UserDetailAPIView.as_view()

class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        # return super().perform_update(serializer)
        instance = serializer.save() 

user_update_view = UserUpdateAPIView.as_view()

class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

user_destroy_view = UserDestroyAPIView.as_view()