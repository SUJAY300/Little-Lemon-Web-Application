from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet, MenuItemsView, SingleMenuItemView

router = DefaultRouter()
router.register("bookings", BookingViewSet, basename="booking")

urlpatterns = [
    path("menu/", MenuItemsView.as_view(), name="menu-list"),
    path("menu/<int:pk>/", SingleMenuItemView.as_view(), name="menu-detail"),
] + router.urls
