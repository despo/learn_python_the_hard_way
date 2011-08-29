# There can be many types of people...
x = "There are %d types of people." % 10
# Assign binary string literal to binary variable
binary = "binary"
# Assign don't string literal to do_not variable
do_not = "don't"
# Substitute binary and do not variables in sentence - Found two strings within a string
y = "Those who know %s and those who %s." % (binary, do_not)

# print There are 10 types of people
print x
# print Those who know binary and those who don't
print y

#print I said There are 10 types of people - Found a string within a string
print "I said: %r." % x
#print I also said: 'Those who know binary and those who don't.'. - Found a string within a string
print "I also said: '%s'." % y

# Assign False to hilariou
hilarious = False
# Assign Isn't that hoke so funny to joke_evaluation varilable
joke_evaluation = "Isn't that joke so funny?! %r"

# print Isn't that hoke so funny?! False
print joke_evaluation % hilarious

# Assign sentence to w
w = "This is the left side of..."
# Assign sentence to e
e = "a string with a right side."

# Print sentences assigned to w and e
print w + e
