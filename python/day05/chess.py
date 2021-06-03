import requests
from bs4 import BeautifulSoup


def get_data(info):
    if info is None:
        return 'None'
    else:
        return info.get_text().strip()


df = []

for country in ('br', 'eune', 'euw', 'jp', 'kr', 'lan', 'las', 'na', 'oce', 'tr', 'ru'):
    url = "https://lolchess.gg/leaderboards?region={}".format(country)
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text)
    table = soup.find('table', class_="table table-page-1 table-sort-tier")
    rows = table.find_all('tr')

    for row in rows[1:]:
        rank = get_data(row.find('td', class_='rank'))
        summoner = get_data(row.find('a'))
        tier = get_data(row.find('span', class_='tier-name-sm'))
        lp_active = get_data(row.find('td', class_='lp active'))
        winrate = get_data(row.find('td', class_='winrate'))
        toprate = get_data(row.find('td', class_='toprate'))
        played = get_data(row.find('td', class_='played'))
        wins = get_data(row.find('td', class_='wins'))
        tops = get_data(row.find('td', class_='tops'))

        df.append([rank, summoner, tier, lp_active, winrate, toprate, played, wins, tops])

        user_url = row.find('a')['href']
        user_resp = requests.get(user_url)
        user_soup = BeautifulSoup(user_resp.text)
        user_match_history = user_soup.find_all('div', class_='profile__match-history-v2__item placement-1')

        for i in range(len(user_match_history)):
            for img in user_match_history[i].select('img'):
                win_synergy.append(img.get('title'))

while None in win_synergy:
    win_synergy.remove(None)

Chosen_synergy = []
for word in win_synergy:
    if "(Chosen)" in word:
        Chosen_synergy.append(word)

print(Chosen_synergy)
print(win_synergy)
