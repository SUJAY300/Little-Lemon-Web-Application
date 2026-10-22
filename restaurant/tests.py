from datetime import timedelta
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APIClient
from .models import Booking, Menu

User = get_user_model()


class MenuAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu = Menu.objects.create(title="Greek Salad", price="12.50", inventory=20)

    def test_menu_list_is_public(self):
        response = self.client.get("/api/menu/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["title"], "Greek Salad")

    def test_menu_create_requires_authentication(self):
        response = self.client.post(
            "/api/menu/",
            {"title": "Pasta", "price": "14.00", "inventory": 8},
            format="json",
        )
        self.assertEqual(response.status_code, 401)

    def test_authenticated_user_can_create_menu_item(self):
        user = User.objects.create_user(username="tester", password="TestPass!234")
        self.client.force_authenticate(user=user)
        response = self.client.post(
            "/api/menu/",
            {"title": "Pasta", "price": "14.00", "inventory": 8},
            format="json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Menu.objects.filter(title="Pasta").exists())

    def test_menu_detail_returns_item(self):
        response = self.client.get(f"/api/menu/{self.menu.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "Greek Salad")


class BookingAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="bookinguser", password="TestPass!234")
        self.client.force_authenticate(user=self.user)

    def test_authenticated_user_can_create_booking(self):
        response = self.client.post(
            "/api/bookings/",
            {
                "name": "Alex",
                "no_of_guests": 2,
                "booking_date": (timezone.now() + timedelta(days=1)).isoformat(),
                "notes": "Window table",
            },
            format="json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Booking.objects.count(), 1)
        self.assertEqual(Booking.objects.first().created_by, self.user)

    def test_anonymous_user_cannot_create_booking(self):
        self.client.force_authenticate(user=None)
        response = self.client.post(
            "/api/bookings/",
            {
                "name": "Alex",
                "no_of_guests": 2,
                "booking_date": (timezone.now() + timedelta(days=1)).isoformat(),
            },
            format="json",
        )
        self.assertIn(response.status_code, (401, 403))
