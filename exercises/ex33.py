def add_numbers_to_list(numbers, size):
  i = 0
  while i < size:
    print "At the top is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

numbers = []

add_numbers_to_list(numbers, 6)

print "The numbers:"

for num in numbers:
  print num
