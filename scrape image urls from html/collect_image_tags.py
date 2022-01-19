import requests
import os
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse
import re


# failed

#page = requests.get("")

#soup = bs(page.content, 'html.parser')
#soup = bs(page.content, 'html.parser')
# find_all_id = soup.find_all(id='test')
example = open("sample.html")
example = open("e6_example.html.html")

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
    if str(link['src']).startswith("https://static1.e621.net"):
        string_link = str(link['src'])
        
        #remove 'preview/'
        edited_string_link = string_link.replace("preview/", "")

        #change jpg to png

        actual_image_string_link = edited_string_link.replace(".jpg", ".png")
        
        print(actual_image_string_link)
        #print(link['src'])

    #print(link['src'])
    # lol ez
