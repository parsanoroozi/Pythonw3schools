# To delete a file, you must import the OS module, and run its os.remove() function:

import os
f = open('myFile.txt', 'x')
f.close()


os.remove("myFile.txt")

# check if the file exist:

if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")


# remove folder:
# To delete an entire folder, use the os.rmdir() method:
os.rmdir("myfolder")
