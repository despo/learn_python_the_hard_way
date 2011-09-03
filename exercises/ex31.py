print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
  print "There's a giant bear here eating a cheese cake. What do you do?"
  print "1. Take the cake."
  print "2. Screan at the bear."

  bear = raw_input("> ")

  if bear == "1":
    print "The bear eats your face off. Good job!"
  elif bear == "2":
    print "The bear eats your legs off. Good job!"
  else:
    print "Well doing %s is probably better. Bear runs away." % bear
elif door == "2":
  print "You stare into the endless abyss at Cthulhu's retina."
  print "1. Blueberries."
  print "2. Yellow jacket clothespins."
  print "3. Understanding revolvers yelling melodies."

  insanity = raw_input("> ")

  if insanity == "1" or insanity == "2":
    print "Your body survives powered by a mind of jello. Good job!"
  else:
    print "The insanity rots your eyes into a pool of much. Good job."

elif door == "X":
  print "I see you've found the secret option..."
  print "There's a big spider in your living room. What do you do?"
  print "1. Scream and run away."
  print "2. Step on it."
  print "3. Grab it with a plastic glove and throw it out."

  spider = raw_input("> ")

  if spider == "1":
    print "You've scared the spider. It runs after you and stinks you. You are dead!"
  elif spider == "3":
    print "Don't be so kind. The spider stinks you through the glove and you die."
  elif spider == "2":
    print "Good job! The spider is now dead, you've won the game!"
  else:
    print "Dead end. Game over for you."

else:
  print "You stumble around and fall on a knife and fie. Good job!"

