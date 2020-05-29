#understanding how while/else works. Else block will execute anytime the loop condition is evaluated to "False"
#Basically in this program random function is being used to generate 3 different numbers separately from 1 to 6(including both)
#if 5 comes u loose

import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
  num = random.randint(1, 6)
  print num
  if num == 5:
    print "Sorry, you lose!"
    break
  count += 1
else:
  print "You win!"
  
  """o/p Lucky Numbers! 3 numbers will be generated.
If one of them is a '5', you lose!
4
1
6
You win!"""