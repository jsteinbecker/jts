from bs4 import BeautifulSoup
import requests
from lxml import etree

url = 'https://www.scrapingbee.com/blog/web-scraping-101-with-python/#2-urllib3--lxml'
tl = requests.get(url)
soup = BeautifulSoup(tl.content,'html.parser')
dom = etree.HTML(str(soup))
dom.xpath('//*[@id="container"]/h1/yt-formatted-string'[0].text)