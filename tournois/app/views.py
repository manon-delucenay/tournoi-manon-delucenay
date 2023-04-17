from django.shortcuts import render, get_list_or_404

from .models import Players, Team, Tournament, Pool, Match


def tournois(request):
    tournois = get_list_or_404(Tournament)
    return render(request, "app/tournois.html", {"tournois": tournois})


def tournoi(request, tournoi_id):
    poules = Pool.objects.filter(tournament=tournoi_id)
    return render(request, "app/tounoi.html", {"poules": poules})
