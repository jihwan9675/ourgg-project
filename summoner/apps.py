from django.apps import AppConfig


class SummonerConfig(AppConfig):
    name = 'summoner'
    game_mode = {'420':'솔랭','430':'일반','440':'자유 5:5 랭크','450':'무작위 총력전','900':'URF','1020':'이벤트'}