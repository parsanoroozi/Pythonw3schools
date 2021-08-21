# read method:

f = open('src/File Handling/FileOpen/test.txt')
print(f.read())
# or you can set how many characters to read

print(f.read(120))

# read lines:
# you can return only one line by using readline:
print(f.readline())

for x in f:
  print(x)
  
  #close files:
  # when you are done with a file, you have to close it