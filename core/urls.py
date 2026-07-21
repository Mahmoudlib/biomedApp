from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('devices/', views.device_list_view, name='device_list'),
    path('devices/<int:pk>/', views.device_detail_view, name='device_detail'),
    path('companies/', views.company_list_view, name='company_list'),
    path('companies/<int:pk>/', views.company_detail_view, name='company_detail'),
    path('offline/', views.offline_view, name='offline'),
]
