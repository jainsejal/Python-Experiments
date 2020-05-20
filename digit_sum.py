# Summing the numbers given in the arguement
def digit_sum(n):
  new = str(n)
  count = 0
  for item in new:
    count = int(item) + count
  return count
print digit_sum(1234)


"""op: 10"""