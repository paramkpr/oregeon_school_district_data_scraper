import requests
import json
from bs4 import BeautifulSoup


def get_links():
    links = []
    url = "http://proximityone.com/or_sdc.htm"
    html = requests.get(url).text

    soup = BeautifulSoup(html, 'html.parser')
    tables = soup.find_all('table')
    link_table = tables[4]
    for row in link_table.find_all('tr'):
        data = row.find_all('td')
        name = data[0].get_text()
        dp1 = data[1].a['href']
        dp2 = data[2].a['href']
        dp3 = data[3].a['href']
        dp4 = data[4].a['href']
        links.append({
            'name': name, 
            'dp1': dp1,
            'dp2': dp2, 
            'dp3': dp3,
            'dp4': dp4
        })

    print(json.dumps(links))

get_links()
