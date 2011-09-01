from sys import argv

script, filename = argv

print "Reading file %r" % filename

target = open(filename, 'r')
print target.read() ,

raw_input("Press any character to close file")
target.close()
