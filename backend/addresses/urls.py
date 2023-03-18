from django.urls import path

from . import views

urlpatterns = [
    path('', views.address_list_create_view),
    path('<int:pk>/', views.address_detail_view),
    path('<int:pk>/update/', views.address_update_view),
    path('<int:pk>/delete/', views.address_destroy_view),
    
]