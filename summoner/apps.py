from django.apps import AppConfig
from riotwatcher import LolWatcher, ApiError
import pandas as pd

class SummonerConfig(AppConfig):
    name = 'summoner'
    
    my_region = 'kr'
    api_key = 'RGAPI-76c6ae14-104e-45bd-8c89-b2922a8c78a0'    
    game_mode = {'420':'솔랭','430':'일반','440':'자유 5:5 랭크','450':'무작위 총력전','900':'URF','1020':'이벤트'}
    champion_name = {}

    versions = watcher.data_dragon.versions_for_region(my_region)
    champions_version = versions['n']['champion']
    current_champ_list = watcher.data_dragon.champions(champions_version)

    def search(self, userName):
        me = watcher.summoner.by_name(my_region, '지은무새')
        my_matches = watcher.match.matchlist_by_account(my_region, me['accountId'])