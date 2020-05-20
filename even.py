# printing only the even numbers on the screen
def purify(s):
  new_list = []
  for item in s:
    if item%2 == 0:
      new_list.append(item)
  return new_list

print purify([2,44,55,88,88,44])

"""o/p : [2,44,88,88,44]"""