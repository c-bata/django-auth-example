from django.urls import path

from socials import views

app_name = 'social'

urlpatterns = [
    path("login/<provider>", views.auth, name="begin"),
    path("complete/<provider>", views.complete, name="complete"),
    path("disconnect/<provider>", views.disconnect, name="disconnect"),
    path("disconnect/<provider>/<int:association_id>", views.disconnect,
         name="disconnect_individual"),
]
