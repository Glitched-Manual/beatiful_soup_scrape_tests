import sys

arg_len = len(sys.argv)

print("Total args passed: ",arg_len)

arg_list = []

file_arg_position = None

count = 0
for arg in sys.argv:
    print("arg[{}]: ".format(count),arg)
    

    arg_list.append(arg)

    if arg == "-f":
        print("file arg passed")

        #mark position of file arg 

        file_arg_position = count

    count = count + 1


if file_arg_position:
    print("file arg found at argv[{}]".format(file_arg_position))

    #check if there is an arg after the file arg

    if arg_len > file_arg_position + 1:
        #check if file ends with html

