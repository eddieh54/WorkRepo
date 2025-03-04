import requests
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np

req_date = input("Enter the date you'd like to view scores for. (year-month-date) ")
url = 'https://sports.yahoo.com/college-basketball/scoreboard/?confId=all&dateRange=' + req_date
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
spreadlist += [np.nan] * (len(df) - len(spreadlist))
df['Spread'] = spreadlist


date = url[-10:]
file_path = date + '.xlsx'
df.to_excel(file_path, date, index = False)





