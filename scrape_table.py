import requests
from bs4 import BeautifulSoup
from pprint import pprint
import pandas as pd

def scrape_table(url, name):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    tables = soup.find_all('table')
    data_table = tables[4]
    data = {'label': [], 'value': [], 'percent': []}
    for row in data_table.find_all('tr'):
        row_data = row.find_all('td')
        data['label'].append(row_data[0].get_text().strip())
        data['value'].append(row_data[1].get_text().strip())
        data['percent'].append(row_data[2].get_text().strip())

    df1 = pd.DataFrame(data)
    print(df1)
    df1.to_csv('data/' + name)

