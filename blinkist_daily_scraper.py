# stolen from https://github.com/theghostofc/Blinkist-Daily-Scraper
# to run, $ python3 blinkist_daily_scraper.py

# coding: utf-8
from bs4 import BeautifulSoup
from datetime import datetime
import os
import tomd
import urllib3
import re
import pathlib
import requests

os.system(f'git pull')

cookies = {
    '__cfduid': 'd747c33cee06bc0eb572437dad105fd5c1606065253',
    'bk_c_n': 'dc099757-6dfd-42b7-a0cf-4edc6cb73ed5',
    'internal_session': 'false',
    'CookieConsent': '{stamp:%27NwhdISJ33KcaATigw0NufrH2I83FKDLlmiyg8Nk8wr4pm78OuHfLEA==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cver:1%2Cutc:1606065257657%2Cregion:%27us%27}',
    '_ga': 'GA1.2.649071746.1606065258',
    '_gid': 'GA1.2.359076828.1606065258',
    '_fbp': 'fb.1.1606065258019.739199592',
    '_scid': 'cc745e45-6469-4122-ab83-3730b1ca2cb2',
    '_hjTLDTest': '1',
    '_hjid': '1d2ed46b-9b3c-409b-934a-51db8bef135e',
    '_pin_unauth': 'dWlkPU56RXlNVEEyTVdRdFlqSTNNaTAwT0RobUxXSXdPR1F0WldObU1tWTRPREZtTVRrNQ',
    '_sctr': '1|1606032000000',
    '_dcmn_p': 'ilgyY2lkPTY2dXVXbC02bkdvTlBGbzFBb1k',
    'modal-leaving-popup': '1',
    'coupon_code': 'freedaily',
    '_pk_ses.1.a1f5': '1',
    '_hjAbsoluteSessionInProgress': '1',
    'timezone': 'America%2FLos_Angeles',
    '__cf_bm': '5700dc9136a571b6aef79980aff2a7eb4712ab47-1606180049-1800-AYPn66KJ8sMNlgTdP4ZxpNtebBzSXpLalImg3SNxDgyilD0yNl/fpmqtJBjGSaea873TCSzFt75V7t5oFGMAeLVvzgDUJda6anlvLeDLQpL8ebLXrFdNBLI+N9Gn8S6PtGQikRBhlQMLnGSVslc5UWX5c4WqSvrq3QrlZ5pKTuTy5dXrKQShT4XoXJvMWgYT6g==',
    '_blinkist-webapp_session': 'ekVSVzdZOHlWYkJJdW9hMjU0WHh2Zk1iZGVlYjBTbEtlUzROeUtpV000a0pOQ3lqL3FZclpiSExmUi83bHI2eGt2QVhYUjEyd2NBeTQySW9pL2FRTHpPZHVOYmhQUVR3Sk1XUE4zOUdVZ3l5OFlhdlNJelRTcDRUQUxsUmc2RmVRNEFxby90QzArSlorSTgvNmhaVVhBMGpETjRWSUQwUmRSeWkzS0lCSis1V2pITVg1c3NpTVlaTVBONWVTcEZaRWc2KzRGTnYxMjNzaXRsZldKS0ZPbFN6UVRzUVBTTmdyQUc0N0FkSlNEVzFORk1aczc0Qk9QS3l1QWl6Nkg2aUd4eVFTKzBpWXRham42MXpXMlBxNDhEeTVLOG90cnNHL21nekRxcVNnWXZTbnkxa29oWEd2TWU4SjJWdmUzVWRiNmFoVmZDN1NzSlV5MGk5UU1obk5Ha29YMjc0blBxZU5iM0JDMFlnWmFhUmFzdnJqdWl3R1BLSGE2RTQwOVAzalRqU3hJZjczODJZbUNzZ2w4VzJPcUw5dGEyODRDWXhPYjJhdjZMWFdMaz0tLUNTaVJ0VmVEM2t1NDBpS052SVRoMkE9PQ%3D%3D--19e1fec616ed322953963d67d42b3f0d6a9a82d8',
    '_dcmn_su4ivnelbvvjf': '-Lldc2lkPU5ZcndCRi04VnVBTlBGbzFBcWsmZXhwPXFrYTF1ag',
    '_tq_id.TV-63729036-1.258b': 'a4398a5086eafd28.1606065258.0.1606180051..',
    '_pk_id.1.a1f5': 'fb20ad409c6be93c.1606065255.4.1606180394.1606178528.',
}

headers = {
    'authority': 'www.blinkist.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-US,en;q=0.9',
}

http = urllib3.PoolManager(10, headers = headers)
urllib3.disable_warnings()

def get_element_from_request(url, element, class_):
    print("get_element_from_request ", url)
    print("headers = ", headers)
    #response = http.request('GET', url)
    response = requests.get('https://www.blinkist.com/nc/daily', headers=headers, cookies=cookies)
    print("response = ", response)
    soup = BeautifulSoup(response.data.decode('utf-8'), "html5lib")
    print("soup = ", soup)
    return soup.find(element, class_ = class_)

# Get meta data
print("getting daily page")
container = get_element_from_request('https://www.blinkist.com/nc/daily', 'div', "daily-book__grid")
print("got container\n", container) 

title = container.find('h3', 'daily-book__headline').string.strip()
author = container.find('div', 'daily-book__author').string.strip()[3:]
description = container.find('div', 'book-tabs__content-inner').p.contents[1]
cta = container.find('a', 'cta')['href']
burl = f'/books/' + re.sub("/en/nc/daily/reader/", "", cta) 
print(burl)
img_url = container.find('img')['src']

date = datetime.now().strftime('%Y%m%d')

bookfile = "blinkist-daily/" + date + "." 
bookfile = bookfile + re.sub(" ", ".", title) 
bookfile = bookfile + ".By." + re.sub(" ", ".", author) 
bookfile = bookfile  + ".md"

if pathlib.Path(bookfile).exists():
    print(bookfile + " exists")
    exit()

# Get actual content
print("get content")
article = get_element_from_request(f'https://www.blinkist.com{cta}', 'article', 'shared__reader__blink reader__container__content')

# Convert to markdown, add source and dump to a file
print("convert markdown")
output = f'# {title}\n*by {author}*\n\n'
output = output + f'Source: [https://www.blinkist.com{burl}](https://www.blinkist.com{burl})\n\n'
output = output + f'![{title}]({img_url})\n\n'
output = output + f'{description}\n\n'
output = output + f'{tomd.convert(str(article).strip())}'

commitMessage = f'Daily'

print("writing " + bookfile)
with open(bookfile, "w", encoding="utf8") as text_file:
    text_file.write(output)

os.system(f'git add "{bookfile}"')
os.system(f'git commit -m "{commitMessage}"')
os.system(f'git push')
