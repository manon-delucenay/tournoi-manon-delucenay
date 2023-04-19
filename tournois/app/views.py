from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Players, Team, Tournament, Pool, Match


def tournois(request):
    tournois = get_list_or_404(Tournament)
    return render(request, "app/tournois.html", {"tournois": tournois})


def tournoi(request, tournoi_id):
    tournoi = get_object_or_404(Tournament, id=tournoi_id)
    poules = Pool.objects.filter(tournament=tournoi_id).order_by("nb")
    return render(request, "app/tournoi.html", {"tournoi":tournoi,"poules": poules})

def poule(request, poule_id):
    poule = get_object_or_404(Pool,id=poule_id)
    classement = poule.classement
    matchs = Match.objects.filter(pool = poule)
    tournoi = poule.tournament
    context = {"poule": poule,"classement" : classement, "matchs": matchs, "tournoi": tournoi}
    return render(request, "app/poule.html", context)

@login_required
def match(request, match_id):
    match = get_object_or_404(Match, id=match_id)
    return render(request, "app/match.html", {"match":match})