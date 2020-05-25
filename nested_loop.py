#Exercise on nested loop for list in a list
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
  result = []
  for numbers in lists:
    for item in numbers:
      result.append(item)
  return result

print flatten(n)

#o/p: [1,2,3,4,5,6,7,8,9]