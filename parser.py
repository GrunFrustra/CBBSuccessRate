# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 13:25:47 2019

@author: ryang
"""

from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re


gamePage = 'https://www.sports-reference.com/cbb/boxscores/2019-04-08-21-virginia.html'
#class="section_anchor" data-label="Texas Tech (31-7)" 
#id="box-score-basic-texas-tech_link"></span>, 

#bs.find('div', {'id':'bodyContent'}).find_all('a',
#href=re.compile('^(/wiki/)((?!:).)*$'))
html = urlopen(gamePage)
bs = BeautifulSoup(html, 'html.parser')
labels = bs.find_all('span',{'data-label':re.compile('\)$')})
for x in labels:
    print(x)