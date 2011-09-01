# defining function that outputs information about cheese and boxes of crackers count
def cheese_and_crackers(cheese_count, boxes_of_crackers):
  print "You have %d cheeses!" % cheese_count
  print "You have %d boxes of crackers!" % boxes_of_crackers
  print "Man that's enought for a party!"
  print "Get a blanket. \n"

print "We can just give the function numbers directly:"
# calling function using numbers
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# calling function using variables as arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
# adding up numbers - sum used as cheese and and boxes of crackers count
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
# adding up variables with numbers as arguments
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)
