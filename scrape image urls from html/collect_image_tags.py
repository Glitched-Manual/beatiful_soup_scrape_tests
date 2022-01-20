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

def png_check(passed_link):

    


    return True

def jpg_check(passed_link):



    return True

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

            #change jpg to png           
           
            png_link = None
            jpg_link = None

            
            if edited_string_link.endswith(".jpg"):
                
                jpg_link = edited_string_link
                png_link = edited_string_link.replace(".jpg", ".png")

                jpg_request = requests.get(jpg_link)

                if jpg_request.status_code == 200:
                    os.system("wget --no-check-certificate -nc {}".format(jpg_link))

                else:
                    #check if .png works

                    png_request = requests.get(png_link)

                    if png_request.status_code == 200:
                        os.system("wget --no-check-certificate -nc {}".format(png_link))


                    else:
                        print("error pull failed : {} could not be found".format(edited_string_link))

            # startwith .png new
            elif edited_string_link.endswith(".png"):
                jpg_link = edited_string_link.replace(".png", ".jpg")
                png_link = edited_string_link

                png_request = requests.get(png_link)

                if png_request.status_code == 200:
                    os.system("wget --no-check-certificate -nc {}".format(png_link))

                else:
                    #check if .jpg works

                    jpg_request = requests.get(jpg_link)

                    if jpg_request.status_code == 200:
                        os.system("wget --no-check-certificate -nc {}".format(jpg_link))


                    else:
                        print("error pull failed : {} could not be found".format(edited_string_link))

                        
            else:
                #check for pull failed 
                
                print("error pull failed : {} does not match target formats".format(edited_string_link))
                
                
            
            
            

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

arg_count = 0
for arg in sys.argv:
    print("arg[{}]: ".format(arg_count),arg)
    

    arg_list.append(arg)

    if arg == "-f":
        print("file arg passed")

        #mark position of file arg 

        file_arg_position = arg_count

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