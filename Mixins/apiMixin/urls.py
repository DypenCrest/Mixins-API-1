from django.urls import path
from .views import *
urlpatterns = [
    path('customer-list/', CustomerLC.as_view(), name='customer-list' ),
    path('customer-detail/<int:pk>/', CustomerRUD.as_view(), name='customer-detail'),


]