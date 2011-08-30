# import mofule argv from system
from sys import argv

# assign the first argument to script and the second to filename
script, filename = argv

# open the file
txt = open(filename)

# print the filename
print "Here's your file %r:" % filename
# read and print the open file
print txt.read()

print "I'll also ask you to type it again:"
# read from user input the filename
file_again = raw_input('>')

# open the filename
txt_again = open(file_again)

# read and print the open file
print txt_again.read()
