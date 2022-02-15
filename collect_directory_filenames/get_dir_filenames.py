import os
import sys
# get all files in dir

current_directory = os.getcwd()
dir_list = os.listdir(current_directory)

if str(sys.argv[0]) in dir_list:
    dir_list.remove(sys.argv[0])

print(dir_list)

#remove the script file
print(sys.argv[0])
# send to file