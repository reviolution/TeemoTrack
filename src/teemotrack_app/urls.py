from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addSummoner/<str:summoner_name>', views.add_summoner, name='addSummoner'),
    path('debug', views.debug, name='debug'),
]
