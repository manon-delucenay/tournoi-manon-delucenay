from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Players, Team, Tournament, Pool, Match, Comments
from .forms import NewComment


def tournois(request):
    tournois = get_list_or_404(Tournament)
    return render(request, "app/tournois.html", {"tournois": tournois})


def tournoi(request, tournoi_id):
    tournoi = get_object_or_404(Tournament, id=tournoi_id)
    poules = Pool.objects.filter(tournament=tournoi_id).order_by("nb")
    return render(request, "app/tournoi.html", {"tournoi": tournoi, "poules": poules})


def poule(request, poule_id):
    poule = get_object_or_404(Pool, id=poule_id)
    classement = poule.classement
    # matchs = poule.match
    matchs = Match.objects.filter(pool=poule)
    tournoi = poule.tournament
    context = {"poule": poule, "classement": classement,
               "matchs": matchs, "tournoi": tournoi}
    return render(request, "app/poule.html", context)


@login_required
def match(request, match_id):
    match = get_object_or_404(Match, id=match_id)
    commentaires = Comments.objects.filter(match=match)
    return render(request, "app/match.html", {"match": match, "commentaires": commentaires})


def commentaire(request, match_id):
    match = get_object_or_404(Match, id=match_id)
    if request.method == "GET":
        nv_comm = NewComment()
    elif request.method == 'POST':
        nv_comm = NewComment(request.POST)
        nv_comm = nv_comm.save(commit=False)
        nv_comm.author = request.user
        nv_comm.match = match
        nv_comm.save()
        return redirect("app:match", {"match" : match})
    return render(request, "app/nv_comm.html", {"form": nv_comm, "match": match})
