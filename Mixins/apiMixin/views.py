from django.shortcuts import render
from .models import Customer
from .serializers import CustomerSerializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.
class CustomerLC(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers

class CustomerRUD(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers
