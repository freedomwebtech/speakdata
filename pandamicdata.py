import requests
from bs4 import BeautifulSoup
import pandas as pd
from ai import speak
#from forlloptest import i
url = requests.get('https://corona.help/country/india')
soup = BeautifulSoup(url.text,'lxml')
a=soup.select('h2 ')[0].getText().replace("stats","")
for i in range(13):
    b1=soup.select('h2')[i].getText()
    b2=soup.select('p')[i].getText()
    speak(b1 + b2)
