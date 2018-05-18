from django.contrib import admin
from django.urls import path, include

from snippets import views

urlpatterns = [
    path("", views.top, name="top"),
    path("snippets/", include("snippets.urls")),
    path("accounts/", include('accounts.urls')),
    path("social/", include("socials.urls")),
    path('admin/', admin.site.urls),
]
