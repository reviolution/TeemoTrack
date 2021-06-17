from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('createSummonerList/', views.create_summoner_list, name='createSummonerList'),
    path('debug', views.debug, name='debug'),
]
