
from bs4 import BeautifulSoup
import json
import requests


def getUserData(nickname: str):
    url = f'https://www.op.gg/summoner/userName={nickname}'
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, 'html.parser')

    data = json.loads(
        str(soup.select_one("script#__NEXT_DATA__").contents[0])
    )['props']['pageProps']['data']
    games = json.loads(
        str(soup.select_one("script#__NEXT_DATA__").contents[0])
    )['props']['pageProps']['games']['data']
    print(len(games));
    tier_data = data['league_stats'][0]['tier_info']

    return {
        'id': data["summoner_id"],
        'name': data['name'],
        'profile_image': data['profile_image_url'],
        'level': data['level'],
        'tier_class': tier_data["tier"],
        'division': tier_data["division"],
        'league_points': tier_data["lp"],
    }


# print(getUserData('akaps'))
# print(getUserData('괴물쥐'))
print(getUserData('섭섭한 틀니'))
