import requests
import os
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse
import re
import datetime
import time
import random


# failed

#page = requests.get("")

extensions = [".jpg",".png"]

#example = open("e6_example.html")

example = open("e6_pull_test.html")

soup = bs(example, 'html.parser')
#print(soup)
for p in example:
    print(p)


#targets = soup.find("tag", {"img"})
#targets = soup.img

targets = soup.find_all("img")

#print(targets)
current_time = datetime.datetime.now()
count = 0

for link in targets:
    #get all

    if count > 1:
        sleep_time = random.randint(10,26)
        time.sleep(sleep_time)

    if str(link['src']).startswith("https://static1.e621.net"):
        string_link = str(link['src'])
        
        #remove 'preview/'
        edited_string_link = string_link.replace("preview/", "")

        #change jpg to png
        
        # check for actual extenstion
        image_request = requests.get(edited_string_link)

        jpg_link = edited_string_link.replace(".jpg", ".png")

        if image_request.status_code == 200:
            os.system("wget --no-check-certificate -nc {}".format(edited_string_link))
        else:
            jpg_request = requests.get(jpg_request)
            
            if image_request.status_code == 200:
                os.system("wget --no-check-certificate -nc {}".format(edited_string_link))
            
            else:
                print("error pull failed")

        actual_image_string_link = edited_string_link.replace(".jpg", ".png")
        
        print(actual_image_string_link)

    count = count + 1
        #print(link['src'])

    #print(link['src'])
    # lol ez

print("*************************")
print("\tprocess completed")
print("*************************")