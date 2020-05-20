# using enumerate function. supply index to each corresponding items in the list and index increasing as we move to next upcoming items
choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
  print index + 1, item

"""o/p: Your choices are:
1 pizza
2 pasta
3 salad
4 nachos"""  