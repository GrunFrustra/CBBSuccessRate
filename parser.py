# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 13:25:47 2019

@author: ryang
"""

from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import teamStats

#URL leads to game data at sports-reference
dayPage = 'https://www.sports-reference.com/cbb/boxscores/index.cgi?month=11&day=15&year=2018'
gamePage = 'https://www.sports-reference.com/cbb/boxscores/2019-03-24-14-clemson.html'


#Strip tag data away to get team names
def getTeamNames(bs):
    labels = bs.find_all('span',{'data-label':re.compile('\)$')})
    teams = []
    for x in labels:
        team_with_record = x['data-label']
        team_name = re.sub('\(.*\)','', team_with_record)
        team_name = team_name.strip()
        teams.append(team_name)
    return teams

#Use BeautifulSoup to get table data, then call appropriate functions
def getTeamData(bs, t1, t2):
    labels = bs.find_all('tfoot')
    print(labels[0])
    print(labels[1])
    t1.fillValues(labels[0])
    t2.fillValues(labels[1])


dayhtml = urlopen(dayPage)
daybs = BeautifulSoup(dayhtml, 'html.parser')
boxscores = daybs.find_all('td',{'class':'right gamelink'})
gameUrls = []
for element in boxscores:
    #/cbb/boxscores/2018-11-15-19-cornell.html
    gamePage = 'https://www.sports-reference.com' + element.find('a')['href']
    print(gamePage)

html = urlopen(gamePage)
bs = BeautifulSoup(html, 'html.parser')

teams = getTeamNames(bs)
print(teams)

team1_data = teamStats.Stats(teams[0])
team2_data = teamStats.Stats(teams[1])
getTeamData(bs, team1_data, team2_data)

team1_data.determineSuccessRate(team2_data)
team2_data.determineSuccessRate(team1_data)

team1_data.printValues()
team2_data.printValues()
#print(team1_data.name)
#print(team1_data.field_goals_made)
#print(team1_data.field_goals_attempted)
#print(team1_data.fouls)
#print(team1_data.steals)
#print(team1_data.turnovers)
#print("SUCCESS RATE")
#print(team1_data.successRate)
