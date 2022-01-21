import requests
import os
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse
import re
import datetime
import time
import random
import sys

class PullOptions:
    def __init__(self, html_file = None, target_directory = None):
        self.html_file = html_file        
        self.target_directory = target_directory

    def set_html_file(self, passed_html_file):
        self.html_file = passed_html_file

    def get_html_file(self):
        return self.html_file

    def get_target_directory(self):
        return self.target_directory

    #self.file_ar

def png_check(passed_png_link, opt_obj = None):
    png_request = requests.get(passed_png_link)

    if png_request.status_code == 200:
        os.system("wget --no-check-certificate -nc {}".format(passed_png_link))
        return True


    return False

def jpg_check(passed_jpg_link, opt_obj = None):

    jpg_request = requests.get(passed_jpg_link)

    if jpg_request.status_code == 200:
        os.system("wget --no-check-certificate -nc {}".format(passed_jpg_link))
        return True


    return False

def webm_check(passed_link, opt_obj = None):
    x = passed_link.rindex('.')
    filebase_link = passed_link[:x]

    webm_link = filebase_link + ".webm"

    webm_request = requests.get(webm_link)

    if webm_request.status_code == 200:

        os.system("wget --no-check-certificate -nc {}".format(webm_link))

        return True 

    return False

def pull_images_from_file_links(passed_filename):
    # failed

    #page = requests.get("")

    extensions = [".jpg",".png"]

    #example = open("e6_example.html")

    example = open(passed_filename)

    soup = bs(example, 'html.parser')
    #print(soup)
    
    targets = soup.find_all("img")

    #print(targets)
    
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

            #remove extension from link
            extension_dot_pos = edited_string_link.rindex('.')

            no_extension_link = edited_string_link[:extension_dot_pos]

            #change jpg to png           
           
            png_link = no_extension_link + ".png"
            jpg_link = no_extension_link + ".jpg"

            if jpg_check(jpg_link):
                print("jpg file downloaded")

            elif png_link(png_link):
                print("png file downloaded")

            elif webm_check(png_link):
                print("webm file downloaded")
            
            else:
                print("error could not find a file for {}".format(string_link))         
            
                
                
            
            
            

        count = count + 1
            #print(link['src'])

        #print(link['src'])
        # lol ez

    print("*************************")
    print("\tprocess completed")
    print("*************************")

arg_len = len(sys.argv)

print("Total args passed: ",arg_len)

arg_list = []

file_arg_position = None

# directory options
directory_arg_position = None
directory_for_output = None


arg_count = 0
for arg in sys.argv:
    print("arg[{}]: ".format(arg_count),arg)
    

    arg_list.append(arg)
    # check for html file arg
    if arg == "-f":
        print("file arg passed")

        #mark position of file arg 

        file_arg_position = arg_count

    if arg == "-d":
        print("directory arg passed")

        directory_arg_position = arg_count

        if arg_len > directory_arg_position + 1:
            directory_for_output = sys.argv[directory_arg_position + 1]


    arg_count = arg_count + 1


if file_arg_position:
    print("file arg found at argv[{}]".format(file_arg_position))

    #check if there is an arg after the file arg

    if arg_len > file_arg_position + 1:
        #check if file ends with html
        filename = sys.argv[file_arg_position + 1]

        if filename.endswith(".html"):
            print("html file found")

            
            # do process
            try:
                pull_images_from_file_links(filename)
            except:
                print(": pull_images_from_file_links() failed - badly")

        else:
            print(sys.exc_info())
            print("error: file provided is not a \'.html\' file")

else:
    print("please provide a e621 posts page")
    print("ie: code -f post_page.html")