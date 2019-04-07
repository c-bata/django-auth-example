from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from snippets import views as snippet_views
from snippets import api_views as snippet_api_views

router = routers.DefaultRouter()
router.register(r'snippets', snippet_api_views.SnippetViewSet)

urlpatterns = [
    path("", snippet_views.top, name="top"),
    path("snippets/", include("snippets.urls")),
    path("accounts/", include('accounts.urls')),
    path("social/", include("socials.urls")),
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
]
