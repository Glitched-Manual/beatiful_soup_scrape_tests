#!/usr/bin/env python
import os

print("enter folder path")

path_to_folder = input()

if path_to_folder.endswith('/') is False:
    path_to_folder = path_to_folder + '/'

#get filenames



file_list = os.listdir(path_to_folder + "html_pages")

# open command file

f = open("./my_command.txt","w")

for target_file in file_list:

	command = "python3 ./script_folder/e6_pull.py -f " + str(path_to_folder) + "/html_pages/" + str(target_file) + " -d " + str(path_to_folder)
	f.write(command + "\n")
	
f.close()