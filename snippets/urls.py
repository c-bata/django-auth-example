from django.urls import path

from snippets import views

urlpatterns = [
    path("new/", views.new_snippet, name="new_snippet"),
    path("<int:snippet_id>/", views.snippet_detail, name="snippet_detail"),
    path("<int:snippet_id>/edit", views.edit_snippet, name="snippet_edit"),
    path("<int:snippet_id>/comments", views.new_comment, name="new_comment"),
]
