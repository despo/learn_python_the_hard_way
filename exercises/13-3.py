from sys import argv

script, name = argv

print 'How old is %r:' % name,
age = raw_input()

print '%s is %r years old' % (name, age)

