from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from . import db_operations
from .models import Summoner, SummonerList
from teemotrack.settings import DEBUG

# Create your views here.

def index(request):
    return render(request, 'teemotrack_app/index.html')

def debug(request):
    if not DEBUG:
        return HttpResponse('Nice try ;)')
    return render(request, 'teemotrack_app/debug.html')


def create_summoner_list(request):
    try:
        name = request.POST['name']
        summoners = request.POST['summoners']
    except ():
        return HttpResponse('xd')

    summ_list = db_operations.create_summoner_list(name, summoners)
    return HttpResponseRedirect('/list/' + summ_list.name)
