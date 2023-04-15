from django.db import models

# Create your models here. 
class Match(models.Model):
    time = models.DateTimeField()
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE)
    score1 = models.IntegerField()
    score2 = models.IntegerField()
    poule = models.PositiveIntegerField()

class Players(models.Model):
    name = models.CharField(max_length=150)
    
class Team(models.Model):
    name = models.CharField(max_length=100)
    trainer = models.CharField(max_length=200)
    teammates = models.ManyToManyField(Players)
    
class Poule(models.Model):
    nb = models.IntegerField()
    tournament = models.CharField(max_length=100)
    teams = models.ManyToManyField(Team)

class Tournament(models.Model):
    name = models.CharField(max_length=200)
    teams = models.ManyToManyField(Team)
    nb_poules = models.IntegerField()
    team_per_poules = models.IntegerField()
    place = models.CharField(max_length=100, blank=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
