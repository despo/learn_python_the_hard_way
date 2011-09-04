def add_numbers_to_list(size, increment=1):
  i = 0
  while i < size:
    print "At the top is %d" % i
    numbers.append(i)

    i = i + increment
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

def print_numbers():
  print "The numbers:"

  for num in numbers:
    print num

# extra credit 2
numbers = []
add_numbers_to_list(6)
print_numbers()

numbers = []
add_numbers_to_list(3)
print_numbers()

# extra credit 4
numbers = []
add_numbers_to_list(3, 2)
print_numbers()

numbers = []
add_numbers_to_list(15, 3)
print_numbers()
