# counting the occurance of the item in the list
def count(seq, item):
  total = 0
  for i in seq:
    if i == item:
      total = total + 1
  return total

print count([1, 2, 1, 1], 1)

"""o/p: 3""" 