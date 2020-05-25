# List comprehension
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50
doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]

# Complete the following line. Use the line above for help.
even_squares = [i **2 for i in range(1,12) if i % 2 == 0]
print even_squares

#the cubed number should be evenly divisible by 4, not the original number.
cubes_by_four = [i ** 3 for i in range(1, 11) if (i ** 3) % 4 == 0]
print cubes_by_four

#Slicing the list
l = [i ** 2 for i in range(1, 11)]

# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print l[2:9:2]

#Use a list comprehension to create a list, threes_and_fives, that consists only of the numbers between 1 and 15 (inclusive) that are evenly divisible by 3 or 5.
threes_and_fives = [i for i in range(1,16) if i%3 == 0 or i%5 == 0]
print threes_and_fives

#reverse thr given string by 2
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-2]
print message