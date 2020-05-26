# Iterating through the list using range function
n = [3, 5, 7]
def total(numbers):
  result = 0
  for item in range(len(numbers)):
    result += numbers[item]
  return result