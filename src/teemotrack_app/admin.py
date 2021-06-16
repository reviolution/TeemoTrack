from django.contrib import admin

from .models import Summoner, RankDataPoint

# Register your models here.
admin.site.register(Summoner)
admin.site.register(RankDataPoint)