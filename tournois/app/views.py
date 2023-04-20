from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Players, Team, Tournament, Pool, Match, Comments
from .forms import CommentForm


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
    matchs = Match.objects.filter(pool=poule)
    tournoi = poule.tournament
    context = {"poule": poule, "classement": classement,
               "matchs": matchs, "tournoi": tournoi}
    return render(request, "app/poule.html", context)

def match(request, match_id):
    match = get_object_or_404(Match, id=match_id)
    commentaires = Comments.objects.filter(match=match)
    return render(request, "app/match.html", {"match": match, "commentaires": commentaires})

@login_required
def commentaire(request, match_id):
    match = get_object_or_404(Match, id=match_id)
    commentaires = Comments.objects.filter(match=match)
    if request.method == "GET":
        nv_comm = CommentForm()
    elif request.method == 'POST':
        nv_comm = CommentForm(request.POST)
        nv_comm = nv_comm.save(commit=False)
        nv_comm.author = request.user
        nv_comm.match = match
        nv_comm.save()
        return redirect("app:match", match_id=match_id)
    return render(request, "app/nv_comm.html", {"form": nv_comm, "match": match, "commentaires": commentaires})

@login_required
def mod_commentaire(request, match_id, commentaire_id):
    match = get_object_or_404(Match, id=match_id)
    commentaires = Comments.objects.filter(match=match)
    comm = get_object_or_404(Comments, id=commentaire_id)
    if request.method == "GET":
        form = CommentForm(instance=comm)
    elif request.method == "POST":
        form = CommentForm(request.POST,instance=comm)
        form.save()
        return redirect("app:match", match_id=match_id)
    return render(request, "app/modif_comm.html", {"form" : form,  "match": match, "commentaires": commentaires, "comm":comm})
