#Live COVID 19 statistics (web scrapping)
import bs4 
import pandas as pd 
import requests 
url = 'https://www.worldometers.info/coronavirus/country/india/'
result = requests.get(url) 
soup = bs4.BeautifulSoup(result.text,'html.parser') #lxml
#search for maincounter-number class 
cases = soup.find_all('div' ,class_= 'maincounter-number') 
# to store data
data = [] 
for i in cases: 
	span = i.find('span') 
	data.append(span.string)
print('Cases', '\tDeaths', '\tRecovered')
print(data, end='\t') 

#dataframe  to visualize
df = pd.DataFrame({"CoronaData": data}) 
#creating coloumns 
df.index = ['TotalCases', ' Deaths', 'Recovered'] 
# storing into Excel 
df.to_csv('Corona_Data.csv')
