from sys import argv

script, input_file = argv

# read (and output) the entire file
def print_all(f):
  print f.read()

# go back to the beginning of the file
def rewind(f):
  f.seek(0)

# print the next line of the file, line count is just a random number we pass in
def print_a_line(line_count, f):
  print line_count, f.readline()

current_file = open(input_file)
print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
