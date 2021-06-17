import cassiopeia as cass
from django.core import serializers
from .models import Summoner, SummonerList, RankDataPoint
import json


def add_summoner(summoner_name: str) -> Summoner:
    cass_summoner = cass.get_summoner(name=summoner_name)
    db_summoner = Summoner(summoner_id=cass_summoner.id, summoner_name=cass_summoner.name)
    db_summoner.save()
    return db_summoner


def create_summoner_list(name: str, summoners: str) -> SummonerList:
    summoner_names = summoners.split(',')
    db_summoners = []

    for summoner_name in summoner_names:
        db_summoners.append(add_summoner(summoner_name))

    summoner_list = SummonerList()
    summoner_list.name = name
    summoner_list.save()
    summoner_list.summoners.set(db_summoners)
    return summoner_list


def get_summoner_list_as_json(name: str) -> str:
    summoner_list = SummonerList.objects.get(name=name)
    list_dict = {'name' : summoner_list.name, 'summoners': {}}
    for summoner in summoner_list.summoners.all():
        list_dict['summoners'][summoner.summoner_name] = []
        for entry in RankDataPoint.objects.filter(summoner=summoner).all():
            entry_dict = {}
            entry_dict['timestamp'] = entry.timestamp.isoformat()
            entry_dict['cumulative_lp'] = entry.cumulative_lp
            entry_dict['division'] = entry.division
            entry_dict['tier'] = entry.tier
            entry_dict['league_points'] = entry.league_points
            list_dict['summoners'][summoner.summoner_name].append(entry_dict)
    return json.dumps(list_dict)
