from rest_framework import generics
from rest_framework import permissions, authentication

from api.mixins import PharmacistPermissionMixin
from .models import User
from .serializers import UserSerializer

    #creating a new user with this view will result in unencrypted password
class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]


    def perform_create(self, serializer):
        return super().perform_create(serializer)
    
user_list_create_view  = UserListCreateAPIView.as_view()


class UserCreateAPIView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        
        return super().post(request, *args, **kwargs)

user_create_view = UserCreateAPIView.as_view()


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

class UserPatchAPIView(
    PharmacistPermissionMixin,
    generics.RetrieveUpdateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

user_patch_view = UserPatchAPIView.as_view()

class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'



user_destroy_view = UserDestroyAPIView.as_view()