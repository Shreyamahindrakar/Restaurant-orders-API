from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.generics import ListAPIView
# Create your views here.

class CreateMenuView(APIView):

    def post(self, request):
        user = request.user
        order = Menu()
        order_serializer = MenuSerializer(order, data=request.data)

        if order_serializer.is_valid():
            order_serializer.save()
            return Response(order_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Menuview(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    lookup_url_kwarg = 'id'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']
    
class SingleMenuView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    lookup_url_kwarg = 'id'
    
class SearchMenuView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['$name_item','$category',"$id"]
    
class OrderStatusView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = (SearchFilter,OrderingFilter)
    search_fields = ['name','date','status']
    
    
    