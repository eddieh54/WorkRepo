import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import date

url = 'https://sports.yahoo.com/college-basketball/scoreboard/?confId=all&dateRange=2025-02-12&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAMtoh4fJ3rCg9UTs6JGQtby2puvhPkJTtFsUr_sAe4bu1EkOGgv46KV0YxvKocPHPSO_QavHRm7SNZOQ8JiIedGaTfs5pHawERnFOzdxP5VMqCLyWhtkJAgV78JhsFPJvIC5oAf4j2NomfmbN3G3W3LnETZjSCJqkrp24dnSzJhf'
data = requests.get(url)

gameinfolist = []
spreadlist = []
team_names = []

html = BeautifulSoup(data.text, 'html.parser')

scoreboard = html.find(id= 'scoreboard-group-2')

games = scoreboard.find_all('div',class_='Fw(b) Fz(14px)')
odds = scoreboard.find_all('div',class_='odds D(i)')
names = scoreboard.find_all('div', class_='Fw(n) Fz(12px)')

def text_to_list(raw, lsname):
    for x in raw:
        x = x.text
        lsname.append(x)

text_to_list(games, gameinfolist)
text_to_list(odds, spreadlist)
text_to_list(names, team_names)

home_team = gameinfolist[1::2]
home_team_name = team_names[1::2]
away_team = gameinfolist[::2]
away_team_name = team_names[::2]

df = pd.DataFrame()

df['Home Team'] = home_team
df['Home Name'] = home_team_name
df['Away Team'] = away_team
df['Away Name'] = away_team_name
df['Spread'] = spreadlist


date = str(date.today())
file_path = date + '.xlsx'
df.to_excel(file_path, date, index = False)


