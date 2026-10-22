from django.shortcuts import render
from rest_framework import permissions, viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.select_related("created_by").all()
    serializer_class = BookingSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        # Authenticated users can see bookings; anonymous users can only GET an empty list.
        if self.request.user.is_authenticated:
            return Booking.objects.select_related("created_by").all()
        return Booking.objects.none()
