from django.urls import path

from socials import views

app_name = 'social'

urlpatterns = [
    path("complete/<provider>", views.complete, name="complete"),
    path("disconnect/<provider>", views.disconnect, name="disconnect"),
]
