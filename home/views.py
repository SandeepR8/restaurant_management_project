from django.shortcuts import render
from .models import restaurant
from rest_framework import generics


class restaurantView(generics.ListAPIView):
    queryset=restaurant.objects.all()
    serializer_class=RestaurantSerializers
