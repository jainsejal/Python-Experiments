# using "," character in after print. makes sure that the next print statement keep on printingon same line
phrase = "A bird in the hand..."

# Add your for loop
for char in phrase:
  if char is "A" or char is "a":
    print "X",
  else:
    print char,
	
	
"""o/p: X   b i r d   i n   t h e   h X n d . . ."""