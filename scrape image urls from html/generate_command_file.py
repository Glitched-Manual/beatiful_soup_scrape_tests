#!/usr/bin/env python3
import os
import sys

print("enter folder path")

path_to_folder = None

try:
	path_to_folder = str(input())
except:
	print(sys.exc_info())

if path_to_folder:
    if path_to_folder.endswith('/') is False:
        path_to_folder = path_to_folder + '/'

    # if path starts with ./
    #
    if path_to_folder.startswith("./"):
        terminal_pwd = os.getcwd()
        path_to_folder.replace("./",terminal_pwd)



    #get filenames




    file_list = os.listdir(path_to_folder + "html_pages")

    # open command file

    f = open("./my_command.txt","w")

    for target_file in file_list:

        command = "e6_image_pull -f " + str(path_to_folder) + "/html_pages/" + str(target_file) + " -d " + str(path_to_folder)
        f.write(command + "\n")
        
    f.close()
else:
    print("error path_to_folder is null")