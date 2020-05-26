# Iterating exercise with string using range function
n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
  result = ""
  for item in range(len(words)):
    result += words[item]
  return result

print join_strings(n)

# o/p Michaelhihhçh