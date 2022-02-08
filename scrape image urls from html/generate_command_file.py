#!/usr/bin/env python3
import os
import sys

directory_arg_position = None
arg_count = 0
directory_path = None
directory_arg_passed = False


def write_command_file(passed_directory):    
    if passed_directory:
        if passed_directory.endswith('/') is False:
            passed_directory = passed_directory + '/'

        # if path starts with ./
        #
        if passed_directory.startswith("./"):
            terminal_pwd = os.getcwd()
            passed_directory.replace("./",terminal_pwd)



        #get filenames

        file_list = os.listdir(passed_directory + "html_pages")

        # open command file

        f = open("./my_command.txt","w")

        for target_file in file_list:
            #trying \" to allow for spaces
            command = "er_media_pull -f \"" + str(passed_directory) + "\"/html_pages/\"" + str(target_file) + "\" -d " + str(passed_directory)
            f.write(command + "\n")
            
        f.close()
    else:
        print("error passed_directory is null")

args_length = len(sys.argv)

for arg in sys.argv:
    if arg == "-d":
        directory_arg_position = arg_count
        directory_arg_passed = True
        print("directory found")
        if args_length > directory_arg_position + 1:
            directory_path = sys.argv[directory_arg_position + 1]


    arg_count = arg_count + 1     

if directory_arg_passed:

    print("yay")
    if directory_path:

        write_command_file(directory_path)

else:



    # if proper args not given do below

    print("enter folder path")

    path_to_folder = None

    try:
        path_to_folder = str(input())
    except:
        print(sys.exc_info())

    write_command_file(path_to_folder)