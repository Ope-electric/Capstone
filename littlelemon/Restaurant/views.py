from django.shortcuts import render
from rest_framework import generics
from .models import Booking, Menu
from .serializers import MenuSerializer
from .serializers import BookingSerializer
from rest_framework import viewsets

# Create your views here.

from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):

    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(
    generics.RetrieveUpdateAPIView,
    generics.DestroyAPIView
):

    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer