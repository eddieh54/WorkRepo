#fieldgoalmadecalculator
import requests
import pandas as pd
from bs4 import BeautifulSoup


url = 'https://www.pro-football-reference.com/years/2023/kicking.htm'
#url2 = 'https://www.teamrankings.com/nfl/stat/opponent-field-goal-attempts-per-game'
data = requests.get(url)
#data2 = requests.get(url2)

statlist = []
Player = []
Games_Played = []
FGA = []
FGCR = []
teamlist = []
fieldgoalmade = []

html = BeautifulSoup(data.text, 'html.parser')
#html2 = BeautifulSoup(data2.text, 'html.parser')

results = html.find(id= 'div_kicking')
#results2 = html2.find(id = 'DataTables_Table_0')

row = results.find_all('td')
#row2 = results2.find_all('tr')

for stat in row:
    player_stats = stat.text
    statlist.append(player_stats)

#for stat2 in row2:
    #team_stats = stat2.text
    #teamlist.append(team_stats)

#29 catagories

def split(a_list, size):
    for i in range(0, len(a_list), size):
        yield a_list[i:i + size]

playerlist = list(split(statlist, 28))

for x in playerlist:
    Player.append(x[0])
    Games_Played.append(x[4])
    FGCR.append(x[19])
    FGA.append(x[16])
    
for x in range(0, len(FGA)):
    FGCR[x] = FGCR[x].rstrip('%')
    print(FGCR[x])
    if FGA[x] == '':
        FGA[x] = FGA[x].replace('','0')
    if FGCR[x] == '':
        FGCR[x] = FGA[x].replace('','0')
    FGPG = int(FGA[x])*(int(float(FGCR[x]))/100)
    fieldgoalmade.append(round(FGPG))

print(FGCR)
print(FGA)

df = pd.DataFrame()
df['Player Name'] = Player
df['Games'] = Games_Played
df['FGA'] = FGA
df['FGCR2'] = FGCR
df['FGM'] = fieldgoalmade

df.to_excel('field_goal6.xlsx', index = False)

print(fieldgoalmade)

#print(Player)
#print(Games_Played)
#print(FGA)
#print(FGCR)




