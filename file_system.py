#working with files that are in the computer
my_list = [i ** 2 for i in range(1, 11)]
# Generates a list of squares of the numbers 1 - 10

f = open("output.txt", "w")

for item in my_list:
  #to write to output.txt file
  f.write(str(item) + "\n")

# to read from the output.txt file
my_file = open("output.txt","r")
print my_file.read()
  
f.close()