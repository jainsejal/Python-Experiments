#taking average of the grades by using fucntion inside the other function
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

# iterating and printing the items in the list grades
def print_grades(grades_input):
  for item in grades_input:
    print item

#computing the sum of the items in grades
def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total

print grades_sum(grades)

#computing the average of the items by calling grades_sum and saving its value in sum_of_grades
def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average

print grades_average(grades)

#computing the variance by calling grades_average and saving its value in average
def grades_variance(scores):
  average = grades_average(scores)
  variance = 0
  for item in scores:
    variance += (average - item) ** 2
    result = variance/len(scores)
  return result

print grades_variance(grades)

#computing the standard deviation 
def grades_std_deviation(variance):
  return variance ** 0.5

#  saving the grades_variance value in variance
variance = grades_variance(grades)
print grades_std_deviation(variance)

#printing all together
for grade in grades:
  print grade
print grades_sum(grades)
print grades_average(grades)
print grades_variance(grades)
print grades_std_deviation(variance)
"""o/p: 1045.5
80.4230769231
334.071005917"""