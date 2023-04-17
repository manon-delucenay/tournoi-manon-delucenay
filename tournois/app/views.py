from django.shortcuts import render, get_list_or_404, get_object_or_404

from .models import Players, Team, Tournament, Pool, Match


def tournois(request):
    tournois = get_list_or_404(Tournament)
    return render(request, "app/tournois.html", {"tournois": tournois})


def tournoi(request, tournoi_id):
    tournoi = get_object_or_404(Tournament, id=tournoi_id)
    poules = Pool.objects.filter(tournament=tournoi_id)
    return render(request, "app/tournoi.html", {"tournoi":tournoi,"poules": poules})

def poule(request, poule_id):
    poule = get_object_or_404(Pool,id=poule_id)
    matchs = Match.objects.filter(pool = poule)
    return render(request, "app/poule.html",{"poule": poule, "matchs": matchs})

def match(request, match_id):
    match = get_object_or_404(Match, id=match_id)
    return render(request, "app/match.html", {"match":match})