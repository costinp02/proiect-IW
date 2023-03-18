from django.urls import path

from . import views

urlpatterns = [
    path('', views.order_list_create_view),
    path('<int:pk>/', views.order_detail_view),
    path('<int:pk>/update/', views.order_update_view),
    path('<int:pk>/delete/', views.order_destroy_view),
    
]