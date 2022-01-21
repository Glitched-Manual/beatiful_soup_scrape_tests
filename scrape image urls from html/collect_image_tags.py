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

debug_messages = False

class PullOptions:
    def __init__(self, html_filename = None, target_directory = None):
        self.html_filename = html_filename        
        self.target_directory = target_directory
            
    def get_html_filename(self):
        return self.html_filename
    
    def get_target_directory(self):
        return self.target_directory


#declaring options object 

def png_check(passed_png_link, opt_obj = None):

    if debug_messages:
        print("--- start png check ---")

        print(passed_png_link)

    png_request = requests.get(passed_png_link)

    if debug_messages:
        print("--- after request ---")

    if png_request.status_code == 200:
        if opt_obj:
            if opt_obj.get_target_directory():
                os.system("wget --no-check-certificate -nc {} --directory-prefix=\"{}\"".format(passed_png_link, str(opt_obj.get_target_directory())))

            else:
                os.system("wget --no-check-certificate -nc {}".format(passed_png_link))

        else:
            os.system("wget --no-check-certificate -nc {}".format(passed_png_link))
        return True

    #print("returned false")
    return False

def jpg_check(passed_jpg_link, opt_obj = None):

    if debug_messages:
        print("--- start jpg check ---")

        print(passed_jpg_link)

    jpg_request = requests.get(passed_jpg_link)

    if debug_messages:
        print("--- after request ---")

    if jpg_request.status_code == 200:
        if opt_obj:
            if opt_obj.get_target_directory():
                os.system("wget --no-check-certificate -nc {} --directory-prefix=\"{}\"".format(passed_jpg_link, str(opt_obj.get_target_directory())))

            else:
                os.system("wget --no-check-certificate -nc {}".format(passed_jpg_link))

        else:
            os.system("wget --no-check-certificate -nc {}".format(passed_jpg_link))
        return True

    if debug_messages:
        print("returned false")
    return False

def webm_check(passed_link, opt_obj = None):

    if debug_messages:
        print("--- start webm check ---")

    x = passed_link.rindex('.')
    filebase_link = passed_link[:x]

    webm_link = filebase_link + ".webm"

    webm_request = requests.get(webm_link)

    if webm_request.status_code == 200:

        if opt_obj:
            if opt_obj.get_target_directory():
                os.system("wget --no-check-certificate -nc {} --directory-prefix=\"{}\"".format(webm_link, str(opt_obj.get_target_directory())))

            else:
                os.system("wget --no-check-certificate -nc {}".format(webm_link))

        else:
            os.system("wget --no-check-certificate -nc {}".format(webm_link))



        return True 

    return False



def pull_images_from_file_links(passed_filename, opt_obj = None):
    # failed

    #page = requests.get("")

    extensions = [".jpg",".png"]

    #example = open("e6_example.html")

    example = open(passed_filename)

    soup = bs(example, 'html.parser')
    #print(soup)
    
    targets = soup.find_all("img")

    if debug_messages:
        print(targets)
    
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

            if debug_messages:

                print(no_extension_link)

            #change jpg to png           
           
            png_link = no_extension_link + ".png"
            jpg_link = no_extension_link + ".jpg"
            webm_link = no_extension_link + ".webm"

            if debug_messages:
                print("------start checks-----")

            if jpg_check(jpg_link, opt_obj):
                print("jpg file downloaded")

            elif png_check(png_link, opt_obj):
                print("png file downloaded")

            elif webm_check(webm_link, opt_obj):
                print("webm file downloaded")
            
            else:
                print("error could not find a file for {}".format(string_link))         
            
                
                
            
            
            

        count = count + 1         
       

    print("*************************")
    print("\tprocess completed")
    print("*************************")

#
# start of code
#

arg_len = len(sys.argv)

if debug_messages:

    print("Total args passed: ",arg_len)


#html file options
file_arg_position = None

# directory options
directory_arg_position = None
directory_for_output = None


arg_count = 0
for arg in sys.argv:
    print("arg[{}]: ".format(arg_count),arg)
  
    # check for html file arg
    if arg == "-f":
        if debug_messages:
            print("file arg passed")

        #mark position of file arg 

        file_arg_position = arg_count

    if arg == "-d":
        if debug_messages:
            print("directory arg passed")

        directory_arg_position = arg_count

        if arg_len > directory_arg_position + 1:
            directory_for_output = sys.argv[directory_arg_position + 1]
            

            


    arg_count = arg_count + 1

# if user provided '-f' option
if file_arg_position:
    if debug_messages:
        print("file arg found at argv[{}]".format(file_arg_position))

    #check if there is an arg after the file arg

    if arg_len > file_arg_position + 1:
        #check if file ends with html
        filename = sys.argv[file_arg_position + 1]


        opt_obj = PullOptions(filename, directory_for_output)
        #print(opt_obj.get_html_filename())
        #print(opt_obj.get_target_directory())

        if debug_messages:
                print(opt_obj.get_html_filename())

        if filename.endswith(".html"):
            if debug_messages:
                print("html file found")

            
            # do process
            try:
                pull_images_from_file_links(filename, opt_obj)
            except:
                print(": pull_images_from_file_links() failed - badly")
                print(sys.exc_info())

        else:
            print(sys.exc_info())
            print("error: file provided is not a \'.html\' file")

else:
    print("please provide a e621 posts page")
    print("ie: code -f post_page.html")