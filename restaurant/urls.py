from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet, MenuViewSet

router = DefaultRouter()
router.register("menu", MenuViewSet, basename="menu")
router.register("bookings", BookingViewSet, basename="booking")

urlpatterns = [
    path("", include(router.urls)),
]
