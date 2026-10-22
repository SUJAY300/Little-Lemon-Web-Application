from django.contrib import admin
from django.urls import include, path
from restaurant.views import home, about

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("admin/", admin.site.urls),
    path("api/", include("restaurant.urls")),
    path("api/auth/", include("djoser.urls")),
    path("api/auth/", include("djoser.urls.authtoken")),
]
