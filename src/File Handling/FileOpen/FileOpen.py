# file handling is an important part of any web applicatoin.
# python has several functions for creating, reading, updating and deleting fules.

# The open() function takes two parameters; filename, and mode.

# There are four different methods (modes) for opening a file:

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists


# In addition you can specify if the file should be handled as binary or text mode

# "t" - Text - Default value. Text mode

# "b" - Binary - Binary mode (e.g. images)

# To open a file for reading it is enough to specify the name of the file:

f = open("src/File Handling/FileOpen/test.txt")
print(f.read())
# The code above is the same as:

f = open("src/File Handling/FileOpen/test.txt", "rt")
# Because "r" for read, and "t" for text are the default values, you do not need to specify them.
