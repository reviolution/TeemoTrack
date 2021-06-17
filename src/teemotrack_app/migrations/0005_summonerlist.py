# Generated by Django 3.2.3 on 2021-06-17 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teemotrack_app', '0004_summoner_last_queried'),
    ]

    operations = [
        migrations.CreateModel(
            name='SummonerList',
            fields=[
                ('name', models.TextField(max_length=64, primary_key=True, serialize=False)),
                ('summoners', models.ManyToManyField(to='teemotrack_app.Summoner')),
            ],
        ),
    ]