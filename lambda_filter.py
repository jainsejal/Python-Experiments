# using lambda function with filter method which takes 2 arguments 
my_list = range(16)
print filter(lambda x: x % 3 == 0)

#Use filter() and a lambda expression to print out only the squares that are between 30 and 70
squares = [x ** 2 for x in range(1,11)]
print filter(lambda x: x > 30 and x <= 70, squares)

# removing "X"s from the given set of string using lambda function
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda i: i != 'X', garbled)
print message