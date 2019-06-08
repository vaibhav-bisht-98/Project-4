from selenium import webdriver
import pandas as pd 
import numpy as np 
from bs4 import BeautifulSoup
import requests
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# chromedriver = 'C:\webdrivers\chromedriver'
# driver = webdriver.Chrome(chromedriver)

stats = pd.DataFrame(columns=['o.s.n','candidate','party','evm_votes','postal_votes','total_votes','percent_votes','constituency'])
stats.set_index('o.s.n',inplace=True)

parser = BeautifulSoup(requests.get('http://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseU051.htm?ac=1').content,'html.parser')
table = parser.select('table')
rows = table[-3].select('tr')

for row in table[-3].select('tr')[3:-2]:
	cells = row.select('td')
	osn = int(cells[0].text)
	stats.loc[osn,'candidate'] = cells[1].text
	stats.loc[osn,'party'] = cells[2].text
	stats.loc[osn,'evm_votes'] = cells[3].text
	stats.loc[osn,'postal_votes'] = cells[4].text
	stats.loc[osn,'total_votes'] = cells[5].text
	stats.loc[osn,'percent_votes'] = cells[6].text
	stats.loc[osn,'constituency'] = table[-3].select('tr')[0].select('th')[0].text.split('-')[-1].strip()

stats.to_csv('chandni_chowk.csv')

