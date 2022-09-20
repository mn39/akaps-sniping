# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import json
import requests
from urllib import parse

user_id = 'Q4xw6CIphLR-0a8qVL5e4X-wSzvLI5cN_otESD5He5ws_Q' #파카
# user_id = "E_KOH2UPZLM8FAjnsiF3u7SpYO92gceCQjJkHriq9BnaMQ" #괴물쥐
# user_id = "Vi4mKv4O3agZUMmDtr3iQzwW615XZzYSsKSEGtwI9FrEKWA" #섭섭한 틀니
endTime = '' #2022-07-20T23:54:41+09:00
summList = {}
summNum = {}

for i in range(100):
    queryList = [('hl', 'ko_KR'), ('game_type', 'TOTAL'), ('ended_at', endTime)]
    query = parse.urlencode(queryList)
    url = f'https://www.op.gg/api/games/kr/summoners/{user_id}?{query}'
    print(url)


    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, 'html.parser')
    soup = json.loads(response.text)
    endTime = soup['meta']['last_game_created_at']

    for j in soup['data']:
        for i in j['participants']:
            if(i['summoner']['summoner_id'] not in summList):
                summList[i['summoner']['summoner_id']] = i['summoner']['internal_name']
                summNum[i['summoner']['summoner_id']] = 1
            else:
                summNum[i['summoner']['summoner_id']] += 1
    

    print(soup['meta'])
    if(soup['meta']['last_game_created_at']==None):
        break

listSort = []
for i in summNum:
    if(summNum[i]==1): continue
    listSort.append([summNum[i],summList[i],i])
listSort.sort()
listSort.reverse()
print(listSort)


# for i in range(10):
#     response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
# soup = BeautifulSoup(response.text, 'html.parser')

# data = json.loads(
#     str(soup.select_one("script#__NEXT_DATA__").contents[0])
# )
# a = json.loads('''''')

# print(url)
# for i in a['data']:
#     print(i['created_at'])
# print(len(a['data']))