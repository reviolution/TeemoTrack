from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.core import serializers
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


def list(request, listname):
    context = {}
    return render(request, 'teemotrack_app/list.html', context)


def create_summoner_list(request):
    try:
        name = request.POST['name']
        summoners = request.POST['summoners']
    except KeyError:
        return HttpResponse('xd')

    summ_list = db_operations.create_summoner_list(name, summoners)
    return HttpResponseRedirect('/list/' + summ_list.name)


def list_redirect(request):
    try:
        listname = request.GET['listname']
    except KeyError:
        return HttpResponse('xd')
    return HttpResponseRedirect('/list/' + listname)


def get_data_for_list(request, listname):
    return HttpResponse(db_operations.get_summoner_list_as_json(listname), content_type="application/json")
