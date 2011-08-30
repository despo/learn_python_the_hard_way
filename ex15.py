print "Type a file you'll like to read:"
# read from user input the filename
file_again = raw_input('>')

# open the filename
txt_again = open(file_again)

# read and print the open file
print txt_again.read()
