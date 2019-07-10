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
        
    def printValues(self, opponent):
        print(self.name)
        print('Field goals made: {}' .format(self.field_goals_made))
        print('Field goals attempted: {}' .format(self.field_goals_attempted))
        print('Steals: {}' .format(self.steals))
        print('Turnovers: {}' .format(self.turnovers))
        print('Fouls: {}' .format(self.fouls))
        print('Success Rate: {0:.2f}' .format(self.successRate))
        print('\n')
        with open('./TeamStats/' + self.name + '.txt', 'a') as f:
            f.write(self.name + '\n')
            f.write('Field goals made: {} \n' .format(self.field_goals_made))
            f.write('Field goals attempted: {} \n' .format(self.field_goals_attempted))
            f.write('Steals: {} \n' .format(self.steals))
            f.write('Turnovers: {} \n' .format(self.turnovers))
            f.write('Fouls: {} \n' .format(self.fouls))
            f.write('Success Rate: {0:.2f}' .format(self.successRate))
            f.write('\n\n')
            f.write(opponent.name + '\n')
            f.write('Field goals made: {} \n' .format(opponent.field_goals_made))
            f.write('Field goals attempted: {} \n' .format(opponent.field_goals_attempted))
            f.write('Steals: {} \n' .format(opponent.steals))
            f.write('Turnovers: {} \n' .format(opponent.turnovers))
            f.write('Fouls: {} \n' .format(opponent.fouls))
            f.write('Success Rate: {0:.2f}' .format(opponent.successRate))
            f.write('\n----------------------')
            
        