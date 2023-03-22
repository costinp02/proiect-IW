from django.urls import path

from . import views

urlpatterns = [
    path('', views.address_list_create_view, name='address-list'),
    path('<int:pk>/', views.address_detail_view, name='address-detail'),
    path('<int:pk>/update/', views.address_update_view, name='address-update'),
    path('<int:pk>/patch/', views.address_patch_view, name='address-patch'),
    path('<int:pk>/delete/', views.address_destroy_view, name='address-delete'),
    
]