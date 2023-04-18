from django.db import models


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
            for j in range(i, len(self.teams.all())):
                if j!=i: matchs.append((self.teams.all()[i], self.teams()[j]))
        return matchs


class Match(models.Model):
    time = models.DateTimeField()
    teams = models.ManyToManyField(Team)
    score1 = models.IntegerField()
    score2 = models.IntegerField()
    pool = models.ForeignKey(Pool, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pool) + ": " + self.teams.all()[0] + " VS " + self.teams.all()[1]
