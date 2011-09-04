i = 0
numbers = []

while i < 6:
  print "At the top is %d" % i
  numbers.append(i)

  i = i + 1
  print "Numbers now: ", numbers
  print "At the bottom i is %d" % i

print "The numbers:"

for num in numbers:
  print num


def add_numbers(size):
  numbers = []
  i = 0
  while i < size:
    print "At the top is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

    print "The numbers:"

    for num in numbers:
      print num

#add_numbers_and_increment_list(3,1)
#print_numbers()

#add_numbers_and_increment_list(9,1)
#print_numbers()

#add_numbers_and_increment_list(3,1)
#print_numbers()
