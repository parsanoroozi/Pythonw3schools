# To write to an existing file, you must add a parameter to the open() function:
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content

# append
f = open('src/File Handling/FileOpen/test.txt', 'a')
f.write("Now the file has more content!")
f.close()

# open and read the file after the appending:
f = open('src/File Handling/FileOpen/test.txt')
print(f.read())

# write
f = open('src/File Handling/FileOpen/test.txt', 'w')
f.write("Now the file has more content!")
f.close()

# open and read the file after the appending:
f = open('src/File Handling/FileOpen/test.txt')
print(f.read())

#create a new file
# to create a new file use the open() method with one of the following parameters:
# "x" - Create - will create a file, returns an error if the file exist

# "a" - Append - will create a file if the specified file does not exist

# "w" - Write - will create a file if the specified file does not exist

f = open('myFile.txt', 'x')
f.close()
