from django.db import models


class Summoner(models.Model):
    summoner_name = models.TextField()
    summoner_id = models.TextField(primary_key=True)


class RankDataPoint(models.Model):
    Summoner = models.ForeignKey(Summoner, on_delete=models.CASCADE)
    Timestamp = models.DateTimeField()
    Cumulative_LP = models.IntegerField()
    Division = models.IntegerChoices('Division', 'I II III IV')
    Tier = models.TextChoices('Tier', 'UNRANKED IRON BRONZE SILVER GOLD PLATINUM DIAMOND MASTER GRANDMASTER CHALLENGER')
    league_points = models.IntegerField()
