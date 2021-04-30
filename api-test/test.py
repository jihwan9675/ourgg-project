from riotwatcher import LolWatcher, ApiError
import pandas as pd
#qNNMCFXnnNdbzjLVonD5LaYzZ7o9K-E0lf5ODQ_PacmiPUs
# golbal variables
api_key = 'RGAPI-38bc37b7-06f5-499b-9e16-86ff595c4019'
watcher = LolWatcher(api_key)
my_region = 'kr'
champ = []
champdic = {}
gamemode = {}

gamemode['420'] = '솔랭'
gamemode['430'] = '일반'
gamemode['440'] = '자유 5:5랭크'
gamemode['450'] = '무작위 총력전'
gamemode['900'] = 'URF'
gamemode['1020'] = '이벤트'
# First we get the latest version of the game from data dragon
versions = watcher.data_dragon.versions_for_region(my_region)
champions_version = versions['n']['champion']

# Lets get some champions
current_champ_list = watcher.data_dragon.champions(champions_version)
# print(current_champ_list['data'])

for data in current_champ_list['data']:
    champ.append(data)
    champdic[current_champ_list['data'][data]['key']] = data

me = watcher.summoner.by_name(my_region, '지은무새')
print(me)
my_matches = watcher.match.matchlist_by_account(my_region, me['accountId'])

# print(my_matches)
# fetch last match detail

# last_match = my_matches['matches'][0]
# match_detail = watcher.match.by_id(my_region, last_match['gameId'])

# print(my_matches['matches'])
# for data in my_matches['matches']:
# print(champdic[str(data['champion'])], gamemode[str(data['queue'])])
# https://ddragon.leagueoflegends.com/cdn/10.6.1/img/champion/{ champdic[str(data['champion'])] }.png


# print(match_detail)
# for data in match_detail['participants']:
#     data[]
# print(match_detail['participantIdentities'])
# print(match_detail)
for idx, matched_num in enumerate(my_matches['matches']):
    if idx < 5:
        match_detail = watcher.match.by_id(my_region, matched_num['gameId'])

        playerInfo = [[],[]]
        
        for player in match_detail['participantIdentities']:
            # participants_row['accountId'] = player['player']['accountId']
            # participants_row['name'] = playerName[i]
            playerInfo[0].append(player['player']['summonerName'])
            playerInfo[1].append(player['player']['accountId'])

        participants = []
        for i, row in enumerate(match_detail['participants']):
            participants_row = {}
            participants_row['name'] = playerInfo[0][i]
            participants_row['accountId'] = playerInfo[1][i]
            participants_row['champion'] = row['championId']
            participants_row['spell1'] = row['spell1Id']
            participants_row['spell2'] = row['spell2Id']
            participants_row['win'] = row['stats']['win']
            participants_row['kills'] = row['stats']['kills']
            participants_row['deaths'] = row['stats']['deaths']
            participants_row['assists'] = row['stats']['assists']
            participants_row['totalDamageDealt'] = row['stats']['totalDamageDealt']
            participants_row['champLevel'] = row['stats']['champLevel']
            participants_row['totalMinionsKilled'] = row['stats']['totalMinionsKilled']
            participants_row['item0'] = row['stats']['item0']
            participants_row['item1'] = row['stats']['item1']
            participants_row['item2'] = row['stats']['item2']
            participants_row['item3'] = row['stats']['item3']
            participants_row['item4'] = row['stats']['item4']
            participants_row['item5'] = row['stats']['item5']
            participants_row['item6'] = row['stats']['item6']
            participants.append(participants_row)
            
        df = pd.DataFrame(participants)
        print(df)
