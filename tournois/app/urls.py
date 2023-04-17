from django.urls import path

from . import views

app_name = "app"
urlpatterns = [
    path("", views.tournois, name="tournois"),
    path("<int:tournoi_id>/", views.tournoi, name="tournoi")
]
