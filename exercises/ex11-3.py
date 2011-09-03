print "How far away is the station from your house?",
distance = raw_input()

print "How long do you need to walk this distance?",
time = raw_input()

pace = int(distance)*1.0/int(time)*1.0

print "I wonder if row_input is read as a string... %r" % pace
