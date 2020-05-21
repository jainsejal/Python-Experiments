start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for items in start_list:
  items = items ** 2
  square_list.append(items)


square_list.sort()
print square_list

[1, 4, 9, 16, 25]