import cassiopeia as cass
from .models import Summoner, SummonerList


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
