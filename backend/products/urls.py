from django.urls import path

from . import views 

urlpatterns = [
    path('', views.product_list_view, name='product-list'),
    path('<int:pk>/', views.product_detail_view, name='product-detail'),
    path('<int:pk>/update/', views.product_update_view, name='product-update'),
    path('<int:pk>/patch/', views.product_patch_view, name='product-patch'),
    path('<int:pk>/delete/', views.product_destroy_view, name='product-delete'),
    
]