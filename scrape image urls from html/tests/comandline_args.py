import sys

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


        else:
            print("error: file provided is not a \'.html\' file")





