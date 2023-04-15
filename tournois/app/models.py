from django.db import models

# Create your models here. 
class Players(models.Model):
    name = models.CharField(max_length=150)
    
class Team(models.Model):
    name = models.CharField(max_length=100)
    trainer = models.CharField(max_length=200)
    teammates = models.ManyToManyField(Players)
    
class Pool(models.Model):
    nb = models.IntegerField()
    tournament = models.CharField(max_length=100)
    teams = models.ManyToManyField(Team)
    
class Match(models.Model):
    time = models.DateTimeField()
    teams = models.ManyToManyField(Team)
    score1 = models.IntegerField()
    score2 = models.IntegerField()
    pool = models.PositiveIntegerField()

class Tournament(models.Model):
    name = models.CharField(max_length=200)
    teams = models.ManyToManyField(Team)
    nb_pool = models.IntegerField()
    team_per_pools = models.IntegerField()
    place = models.CharField(max_length=100, blank=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
