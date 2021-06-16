from cassiopeia import data
from cassiopeia.core import summoner
from cassiopeia.data import Rank
from django import db
from .models import Summoner, RankDataPoint
from django_cassiopeia import cassiopeia as cass
from datetime import datetime
import time
import threading

tier_translate = {
    'IRON': 0,
    'BRONZE': 1,
    'SILVER': 2,
    'GOLD': 3,
    'PLATINUM': 4,
    'DIAMOND': 5,
    'MASTER': 6,
    'GRANDMASTER': 6,
    'CHALLENGER': 6,
}

division_translate = {
    'I': 3,
    'II': 2,
    'III': 1,
    'IV': 0,
}

def start_thread():
    thread = threading.Thread(target=main_loop)
    thread.start()


def main_loop():
    while True:
        update_longest_not_updated_summoner()
        time.sleep(60)
    

def update_longest_not_updated_summoner():
    summoner = Summoner.objects.order_by('last_queried')[0]
    save_for_summoner(summoner)


def save_for_summoner(db_summoner: Summoner):
    cass_summoner = cass.Summoner(id=db_summoner.summoner_id)
    db_summoner.last_queried = datetime.now()
    db_summoner.summoner_name = cass_summoner.name
    db_summoner.save()
    ranked = False
    for entry in cass_summoner.league_entries:
        if entry.queue == cass.Queue.ranked_solo_fives:
            league_entry = entry
            ranked = True
            break
    if not ranked:
        return
    data_point = RankDataPoint()
    data_point.summoner = db_summoner
    data_point.tier = league_entry.tier.value
    data_point.division = league_entry.division.value
    data_point.league_points = league_entry.league_points
    data_point.timestamp = datetime.now()
    cum_lp = 0
    cum_lp += tier_translate.get(league_entry.tier.value) * 400
    if league_entry.tier.value not in ('MASTER', 'GRANDMASTER', 'CHALLENGER'):
        cum_lp += division_translate.get(league_entry.division.value) * 100
    cum_lp += league_entry.league_points
    data_point.cumulative_lp = cum_lp
    
    # Only save to db if LP changed or no entry exists
    query = RankDataPoint.objects.filter(summoner=db_summoner).order_by('-timestamp')
    if len(query) == 0 or query[0].cumulative_lp != cum_lp:
        data_point.save()
    
