#using for/else loop. else statement is executed after the for loop but only if for loop ends noamally that is without the break statement
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
  if f == 'tomato':
    print 'A tomato is not a fruit!' # (It actually is.)
  print 'A', f
else:
  print 'A fine selection of fruits!'
  
"""O/p: You have...
A banana
A apple
A orange
A tomato is not a fruit!
A tomato
A pear
A grape
A fine selection of fruits!"""