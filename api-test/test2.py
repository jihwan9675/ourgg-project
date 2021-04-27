from riotwatcher import LolWatcher, ApiError

lol_watcher = LolWatcher('RGAPI-4fcb4354-f0b7-48fd-bb34-f0bbc6e3c91f')

my_region = 'kr'

champ = []
# First we get the latest version of the game from data dragon
versions = lol_watcher.data_dragon.versions_for_region(my_region)
champions_version = versions['n']['champion']

# Lets get some champions
current_champ_list = lol_watcher.data_dragon.champions(champions_version)
# print(current_champ_list['data'])

for data in current_champ_list['data']:
    champ.append(data)
    print(data ,current_champ_list['data'][data]['key'])

# # print(current_champ_list['data']['Zed']['key'])

# for name in champ:
#     print(name,current_champ_list['data'][name]['key'])