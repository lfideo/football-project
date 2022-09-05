import requests
import pandas as pd
pd.set_option('display.max_columns', 30)

res = []
for x in range(1, 7):
    url = "https://api.sofascore.com/api/v1/unique-tournament/17/season/41886/events/round/"f"{x}"

    payload = ""
    headers = {
        "authority": "api.sofascore.com",
        "accept": "*/*",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "origin": "https://www.sofascore.com",
        "referer": "https://www.sofascore.com/",
        "sec-ch-ua": "Chromium;v=104, Not A;Brand;v=99, Google Chrome;v=104",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "macOS",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
    }
    r = requests.request("GET", url, data=payload, headers=headers)
    data = r.json()

    for i in data['events']:
        res.append(i)
    
    pl = pd.json_normalize(res)

pl = pl[['roundInfo.round', 'startTimestamp', 'homeTeam.name', 'awayTeam.name', 'homeScore.display', 'awayScore.display', 'homeScore.period1', 'awayScore.period1', \
    'homeScore.period2', 'awayScore.period2', 'time.injuryTime1', 'time.injuryTime2']]

pl.rename(columns={
    'roundInfo.round': 'round', 'startTimestamp': 'startTime',
    'homeTeam.name': 'homeTeam', 'awayTeam.name': 'awayTeam',
    'homeScore.display': 'homeScore', 'awayScore.display': 'awayScore',
    'homeScore.period1': 'homeTeam1HT', 'awayScore.period1': 'awayTeam1HT',
    'homeScore.period2': 'homeTeam2HT', 'awayScore.period2': 'awayTeam2HT',
    'time.injuryTime1': 'injuryTime1', 'time.injuryTime2': 'injuryTime2'
}, inplace=True
)

pl.startTime = pd.to_datetime(pl.startTime, unit='s')