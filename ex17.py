from sys import argv
from os.path import exists

script, from_file, to_file = argv

input = open(from_file)
indata = input.read()

print "Does the output file exist? %r" % exists(to_file)
print "Copying  %d bytes of data from %s to %s" % (len(indata), from_file, to_file)

output = open(to_file, 'w')
output.write(indata)

print "Alright, all done."

output.close()
input.close()
