the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'appricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this kind of a for-loop goes through a list
for number in the_count:
  print "This is count %d" % number

# same as above
for fruit in fruits:
  print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what it is
for i in change:
  print "I got %r" % i

# we can also build lists, first start with an empty one
elements = range(0, 6)

# now we can print them out too
for i in elements:
  print "Element was: %d" % i
