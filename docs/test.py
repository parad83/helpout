from bs4 import BeautifulSoup
import requests
import csv

URL = 'https://www.polskawliczbach.pl/Miasta'
PATH = '/Users/parad/mysql/secure/data.csv'     # path to a directory from which MySQL can import data
HEADERS = ['Name', 'Voivodeship', 'Population']

r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html.parser')

table = soup.tbody      # finds table on the page
rows = table.find_all('tr')     

with open(PATH, 'w', encoding='utf8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=HEADERS)
    writer.writeheader()
    for r in rows:          # row of the table
        data = r.find_all('td')
        name = (data[1].select_one('a')).get_text()     # name of the city
        voiv = data[3].get_text().capitalize()          # voivodeship 
        pop = data[4].get_text()                        # population
        
        row = {'Name': name, 'Voivodeship': voiv, 'Population': int("".join(pop.split()))}
        writer.writerow(row)        # writes data into the csv file

# # # string = 'Mi\\u0144sk'

# # # print(string)
# # # print(string.encode('utf-16').decode('utf-16'))


# import requests

# URL = 'https://api.um.warszawa.pl/api/action/datastore_search?resource_id=400a1733-d8e3-4995-943d-ae6468885124'  

# data = requests.get(URL)

# print(data.content)

# from datetime import datetime, date

# def days_since(value):
#     value = datetime.strptime(value, '%Y/%m/%d %H:%M')
#     delta = datetime.now()-value
#     if delta.days < 1:
#         return 'today, {}'.format(value.time())
#     elif delta.days < 2:
#         return 'yesterday, {}'.format(value.time())
#     else:
#         return value.strftime('%d/%m/%Y')


# print(days_since('2022/10/01 21:13'))

from urllib.parse import urlparse

LINK_LIST = '/Users/parad/IES/CS/IA/media/link_list.txt'

url = 'https://www.instagram.com/betsyjohnson_/'

with open(LINK_LIST, 'r') as f:
    link = urlparse(url)
    print(link.netloc.split('.')[1])
    for line in f:
        if link.netloc in line:
            print('git')
            break
        else:
            print('nie git')

