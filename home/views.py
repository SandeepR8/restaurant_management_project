from django.shortcuts import render
from .models import restaurant


def RestaurantView(request):
    queryset=restaurant.objects.all()
    return render(request,'core/home.html',queryset)
