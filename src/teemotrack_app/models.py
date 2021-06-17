from django.db import models
from datetime import datetime


class Summoner(models.Model):
    summoner_name = models.TextField()
    summoner_id = models.TextField(primary_key=True)
    last_queried = models.DateTimeField(default=datetime.min)


class RankDataPoint(models.Model):
    summoner = models.ForeignKey(Summoner, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    cumulative_lp = models.IntegerField()
    division = models.CharField(max_length=2)
    tier = models.TextField()
    league_points = models.IntegerField()


class SummonerList(models.Model):
    name = models.TextField(max_length=64, primary_key=True)
    summoners = models.ManyToManyField(Summoner)
