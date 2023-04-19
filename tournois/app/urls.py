from django.urls import path

from . import views

app_name = "app"
urlpatterns = [
    path("", views.tournois, name="tournois"),
    path("tournoi/id=<int:tournoi_id>/", views.tournoi, name="tournoi"),
    path("poule/id=<int:poule_id>/", views.poule, name="poule"),
    path("match/id=<int:match_id>/", views.match, name="match"),
    path("match/id=<int:match_id>/nouveau_commentaire/", views.commentaire, name="nv_comm"),
    path("match/id=<int:match_id>/modifier_commentaire/id=<int:commentaire_id>", views.mod_commentaire, name = "modif_comm")
]
