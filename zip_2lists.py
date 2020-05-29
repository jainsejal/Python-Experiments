#working with zip. can iterate between 2 or more lists. creates pair of items and will stop at the end of the shortest lists
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
  # Add your code here!
    print max(a, b)
	
	
"""o/p: 
19
19
19
19
19"""