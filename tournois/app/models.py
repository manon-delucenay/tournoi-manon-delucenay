from django.db import models
from django.contrib.auth.models import User

class Players(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    trainer = models.CharField(max_length=200)
    teammates = models.ManyToManyField(Players)

    def __str__(self):
        return self.name


class Tournament(models.Model):
    name = models.CharField(max_length=200)
    teams = models.ManyToManyField(Team)
    nb_pool = models.IntegerField()
    team_per_pools = models.IntegerField()
    place = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class Pool(models.Model):
    nb = models.IntegerField()
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    teams = models.ManyToManyField(Team)

    def __str__(self):
        return str(str("Poule ") + str(self.nb))

    def match(self):
        matchs = []
        for i in range(len(self.teams.all())):
            for j in range(i+1, len(self.teams.all())):
                teams = (self.teams.all()[i],self.teams.all()[j])
                if Match.objects.filter(teams = teams):
                    match = Match(pool=self)
                    match.teams.set((self.teams.all()[i],self.teams.all()[j]))
                    match.save()
                    matchs.append(match)
        return matchs

    def classement(self):
        scores = {}
        for team in self.teams.all():
            scores[team] = 0
        matchs = Match.objects.filter(pool = self)
        for match in matchs:
            if match.score1 > match.score2:
                scores[match.teams.all()[0]] += 2
            elif match.score1 < match.score2:
                scores[match.teams.all()[1]] += 2
            elif match.score1 == 0:
                scores[match.teams.all()[0]] += 1
                scores[match.teams.all()[1]] += 1
        teams_ranked = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))
        return teams_ranked


class Match(models.Model):
    time = models.DateTimeField(null=True, blank=True)
    place = models.CharField(max_length=100, null=True, blank=True)
    teams = models.ManyToManyField(Team)
    score1 = models.IntegerField(null=True, blank=True)
    score2 = models.IntegerField(null=True, blank=True)
    pool = models.ForeignKey(Pool, on_delete=models.CASCADE)

    def __str__(self):
        return self.teams.all()[0] + " VS " + self.teams.all()[1]
    
    def display(self):
        return str(self.score1) + " - " + str(self.teams.all()[0]) + " VS " + str(self.teams.all()[1]) + " - " + str(self.score2)

class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=2000)