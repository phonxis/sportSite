from django.db import models

# Create your models here.

class Team(models.Model):
    shortName = models.CharField(unique=True, max_length=30)
    fullName = models.CharField(unique=True, max_length=60)
    nickname = models.CharField(max_length=30)
    image = models.CharField(max_length=60)
    founded = models.DateField()
    ground = models.CharField(max_length=30)
    groundsCapacity = models.IntegerField()
    country = models.CharField(max_length=30)
    league = models.ManyToManyField('League', null=True, blank=True)
    manager = models.CharField(max_length=30, default='manager')
    website = models.URLField()
    matches = models.ManyToManyField('Match', null=True, blank=True)

    def __str__(self):
        return self.shortName

class Match(models.Model):
    date = models.DateField()
    home = models.ForeignKey('Team', related_name='home', verbose_name='Team 1')
    away = models.ForeignKey('Team', related_name='away', verbose_name='Team 2')
    homeGoals = models.IntegerField()
    awayGoals = models.IntegerField()
    league = models.ForeignKey('League')

    def __str__(self):
        return '{0}:{1} - {2}'.format(self.date, self.home, self.away)


class League(models.Model):
    leagueName = models.CharField(max_length=60)
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.leagueName


class ResultTable(models.Model):
    name = models.ForeignKey('Team')
    played = models.IntegerField(default=0)
    won = models.IntegerField(default=0)
    drawn = models.IntegerField(default=0)
    lost = models.IntegerField(default=0)
    forgoals = models.IntegerField(default=0)
    against = models.IntegerField(default=0)
    goalDifferrence = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    season = models.CharField(max_length=30, default='15/16', null=True, blank=True)
    nameLeague = models.ForeignKey('League', null=True, blank=True)
    group = models.CharField(max_length=1, null=True, blank=True)

