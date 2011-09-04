some_methods = ["upcase!", "zip", "between?"]

print  "The ogirinal list:\n %s \n" % some_methods

dup = "dup"
some_methods.append(dup)
print "appending '%s': \n %s\n" % (dup, some_methods)

other_methods = ["collect", "oct", "id", "slice"]
some_methods.extend(other_methods)
print "extend with %s: \n %s\n" % (other_methods, some_methods)

frozen = "frozen?"
position = 3
some_methods.insert(position, frozen)
print "insert '%s' at position '%d': \n %s\n" % (frozen, position, some_methods)

some_methods.remove(frozen)
print "remove '%s': %s\n" % (frozen, some_methods)

some_methods.pop()
print "pop: %s\n" % some_methods

index = some_methods.index(dup)
print "index of %s is %d: %s\n" % (dup, index, some_methods)

print "count of %s in %s is %d\n" % (dup, some_methods, some_methods.count(dup))

some_methods.sort()
print "sort: %s\n" % some_methods

some_methods.reverse()
print "reverse: %s\n" % some_methods
