import requests
import os
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse


# failed

#page = requests.get("")

#soup = bs(page.content, 'html.parser')
#soup = bs(page.content, 'html.parser')
# find_all_id = soup.find_all(id='test')
example = open("sample.html")

soup = bs(example, 'html.parser')
#print(soup)
for p in example:
    print(p)


#targets = soup.find("tag", {"img"})
#targets = soup.img

targets = soup.find_all("img")

#print(targets)

for link in targets:
    #get all    
    print(link['src'])