# using break statement to set the limitation and protect the code from going to infinite loop

count = 0

while True:
  print count
  count += 1
  if count >= 10:
    break
