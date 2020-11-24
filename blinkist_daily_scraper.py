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

headers = {
        'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
        ':authority: www.blinkist.com',
        ':method: GET',
        ':path: /nc/daily',
        ':scheme: https',
        'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding: gzip, deflate, br',
        'accept-language: en-US,en;q=0.9',
        'cache-control: max-age=0',
        'cookie: __cfduid=d747c33cee06bc0eb572437dad105fd5c1606065253; bk_c_n=dc099757-6dfd-42b7-a0cf-4edc6cb73ed5; internal_session=false; CookieConsent={stamp:%27NwhdISJ33KcaATigw0NufrH2I83FKDLlmiyg8Nk8wr4pm78OuHfLEA==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cver:1%2Cutc:1606065257657%2Cregion:%27us%27}; _ga=GA1.2.649071746.1606065258; _gid=GA1.2.359076828.1606065258; _fbp=fb.1.1606065258019.739199592; _scid=cc745e45-6469-4122-ab83-3730b1ca2cb2; _hjTLDTest=1; _hjid=1d2ed46b-9b3c-409b-934a-51db8bef135e; _pin_unauth=dWlkPU56RXlNVEEyTVdRdFlqSTNNaTAwT0RobUxXSXdPR1F0WldObU1tWTRPREZtTVRrNQ; _sctr=1|1606032000000; _dcmn_p=ilgyY2lkPTY2dXVXbC02bkdvTlBGbzFBb1k; _dcmn_p=ilgyY2lkPTY2dXVXbC02bkdvTlBGbzFBb1k; _dcmn_p=ilgyY2lkPTY2dXVXbC02bkdvTlBGbzFBb1k; modal-leaving-popup=1; coupon_code=freedaily; __cf_bm=68d409e2b36baa98cf1a1e77d526c790d123216f-1606178528-1800-ATnTvNSwgTs5wmSaSRU21UujOTNT6wR3/uX3qyifPPwupCjpyXIMoU8IPtBmlaHfCJCgRXhkbzAzlCQYbTaBaOa7y+10Ta8JEHsznmN2srruVluGyAWarzQiABRm4m1gAaFwAd3FJe7/D94yFixhxYKRt7wWOC98MQgG7fbe/JVDNabJb0zG2CcBBLDuTvcUMQ==; _pk_id.1.a1f5=fb20ad409c6be93c.1606065255.4.1606178528.1606178528.; _pk_ses.1.a1f5=1; _blinkist-webapp_session=SGJnM1pJMmZDY09MVUlWM3NxUnE4UmVhc0RUdVA1OGZPdEhCQklHMGQzRTcrUzZnOXFycFZYbTJvUWFHbm42eGlXWWtEaEJxWTlaV0hhSkhYc2NTcUx2TU5MVklMZ2habmhSTUl2azlyTThQWXBLTzlqTlNQTnJSbng1bDBnaHlGRnB2MzVOQVlKTWRZcHJBSk5xcUlMSm9Gam42ZEd5dEJ1VDJnWlFRaTVzMngwVVN2Y3dKUFI1QzR6Tlp5VVRPZGFFL2szZEluTGsrQjZOUGxDTGxMbTRjTlJzL2RoaVZOMnJOZituYzhoeTVsS084dDlvTFpzYmZuekFTUE8vUm9BNFlySEQ3T3VHREw2RG1ENXRtUWZDdGdkOHlHZytiM2puckhnQkF0TEFkeTFvMWpUUGxuTit3UlRuRjkvUEMwdUVpR1ZTeDlUZkxMRUt5R01sOE81NEplWEZXdHJYKzVrSFBRWC9wL0FWcm43TWUvTUZLekJFZnJtdFpQbU8weWptc3pvZk9Ib0NraGNnQThYdzhHQXQ3aGE4ZWdTR2RaeUtKTXNIUHdkMD0tLXR1d1VENFZKYS9BbmtVdUM4YzBIUlE9PQ%3D%3D--f50573127161faccecd5c648be7361b0429c7345; _dcmn_su4ivnelbvvjf=-MAic2lkPU5ZcndCRi04VnVBTlBGbzFBcWsmZXhwPXFrYTBvOQ; _dcmn_su4ivnelbvvjf=-MAic2lkPU5ZcndCRi04VnVBTlBGbzFBcWsmZXhwPXFrYTBvOQ; _dcmn_su4ivnelbvvjf=-MAic2lkPU5ZcndCRi04VnVBTlBGbzFBcWsmZXhwPXFrYTBvOQ; _gat_UA-34503481-1=1; outbrain_cid_fetch=true; _hjAbsoluteSessionInProgress=1; _tq_id.TV-63729036-1.258b=a4398a5086eafd28.1606065258.0.1606178529..',
        'sec-fetch-dest: document',
        'sec-fetch-mode: navigate',
        'sec-fetch-site: none',
        'sec-fetch-user: ?1',
        'upgrade-insecure-requests: 1'
        }

http = urllib3.PoolManager(10, headers = headers)
urllib3.disable_warnings()

def get_element_from_request(url, element, class_):
    print("get_element_from_request " + url)
    #response = http.request("GET", url)
    response = requests.get(url, headers=headers)
    print(response)
    #soup = BeautifulSoup(response.data.decode('utf-8'), "html5lib")
    #print(soup)
    #return soup.find(element, class_ = class_)

# Get meta data
print("getting daily page")
container = get_element_from_request('https://www.blinkist.com/nc/daily', 'div', "daily-book__grid")
print("got container") 

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
