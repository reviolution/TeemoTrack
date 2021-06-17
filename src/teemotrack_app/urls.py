from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/createSummonerList/', views.create_summoner_list, name='createSummonerList'),
    path('api/getDataForList/<str:listname>', views.get_data_for_list, name='getDataForList'),
    path('list/', views.list_redirect, name='list_redirect'),
    path('list/<str:listname>', views.list, name='list'),
    path('debug', views.debug, name='debug'),
]
