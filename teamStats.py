# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 16:24:24 2019

@author: ryang
"""

class Stats():
    def __init__(self, tname):
        self.name = tname
        self.field_goals_made = 0
        self.field_goals_attempted = 0
        self.steals = 0
        self.turnovers = 0
        self.fouls = 0
        self.successRate = 0.0
        
    #Fill Stats with categories needed to calculate Success Rate
    def fillValues(self, statString):
        self.field_goals_made = statString.find('td',{'data-stat':'fg'}).text
        self.field_goals_attempted = statString.find('td',{'data-stat':'fga'}).text
        self.steals = statString.find('td',{'data-stat':'stl'}).text
        self.turnovers = statString.find('td',{'data-stat':'tov'}).text
        self.fouls = statString.find('td',{'data-stat':'pf'}).text
        
    def determineSuccessRate(self, opponent):
        #Successful PLays:
        #fgm
        #opponent fouls
        successes = self.field_goals_made + opponent.fouls
        #Failed Plays:
        #fga - fgm
        #turnovers
        fails = (int(self.field_goals_attempted) - int(self.field_goals_made)) \
            + int(self.turnovers)
        self.successRate = float(successes) / float(fails)
        