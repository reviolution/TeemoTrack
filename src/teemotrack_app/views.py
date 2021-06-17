from django.http.response import HttpResponse
from django.shortcuts import render
from django_cassiopeia import cassiopeia as cass
from .models import Summoner
from teemotrack.settings import DEBUG

# Create your views here.

def index(request):
    return render(request, 'teemotrack_app/index.html')

def debug(request):
    if not DEBUG:
        return HttpResponse('Nice try ;)')
    return HttpResponse('No error lol')

def add_summoner(request, summoner_name):
    cass_summoner = cass.get_summoner(name=summoner_name)
    db_summoner = Summoner(summoner_id=cass_summoner.id, summoner_name=cass_summoner.name)
    db_summoner.save()
    return HttpResponse('Added Summoner ' + db_summoner.summoner_name + ' with id ' + db_summoner.summoner_id)
