from django.urls import path

from . import views

app_name = "app"
urlpatterns = [
    path("", views.tournois, name="tournois"),
    path("<int:tournoi>/", views.tournoi, name="tournoi")
]
