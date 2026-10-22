
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from restaurant.views import home, about

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("admin/", admin.site.urls),
    path("api/", include("restaurant.urls")),
    path("api/auth/", include("djoser.urls")),
    path("api/auth/", include("djoser.urls.authtoken")),
    path("api-token-auth/", obtain_auth_token, name="api-token-auth"),
]
