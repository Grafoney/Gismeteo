import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

url = "https://www.gismeteo.ru/"


def get_html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
    r = requests.get(url, headers=headers)
    return r.text

def parse(html):
    soup = BeautifulSoup(html)
    h2 = soup.find("h2", class_ = "typeC")
    print ('Город:' , h2.text)
    dd = soup.find("dd",class_ = "value m_temp c")
    print ('Температура:' , dd.text)
    div = soup.find('div', class_ = 'wicon hum')
    print(div.text)

    time = datetime.now()
    time = datetime.strftime(datetime.now(), "%H:%M %Y.%m.%d ")

    weatherLog = {"City": h2.text, "Temperature": dd.text[:3], "humidity": div.text[:3], "date": time }
    json_weatherLog = json.dumps(weatherLog)
    print(weatherLog)
    with open('Weatherlog.json', 'w', encoding='utf-8' ) as jsonfile:
        json.dump(weatherLog, jsonfile, ensure_ascii = False)

def main():
    parse(get_html(url))

print(main())
