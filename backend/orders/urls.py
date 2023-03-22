from django.urls import path

from . import views

urlpatterns = [
    path('', views.order_list_create_view, name="order-list"),
    path('<int:pk>/', views.order_detail_view, name="order-detail"),
    path('<int:pk>/update/', views.order_update_view, name="order-update"),
    path('<int:pk>/patch/', views.order_patch_view, name="order-patch"),
    path('<int:pk>/delete/', views.order_destroy_view, name="order-delete"),
    
]