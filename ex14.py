from sys import argv

script, user_name, kingdom = argv
prompt = '% '

print "Hi %s from the kingdom of %s I'm the % script." % (user_name, kingdom, script)
print "I'd like to ask you for a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
