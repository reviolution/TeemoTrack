from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('createSummonerList/', views.create_summoner_list, name='createSummonerList'),
    path('list/', views.list_redirect, name='list_redirect'),
    path('list/<str:listname>', views.list, name='list'),
    path('debug', views.debug, name='debug'),
]
