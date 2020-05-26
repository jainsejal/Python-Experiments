# multiplying items of the list
def product(seq):
  result = 1
  for item in seq:
    result = result * item
  return result
print product([4, 5, 5])

"""o/p: 100"""