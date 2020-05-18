# Computing the area of circle and triangle
option = raw_input("Enter C for Circle or T for Triangle: ")
if option == "C":
  radius = float(raw_input("Enter the value: "))
  area = 3.14159 * radius**2
  print "The area of circle is " + str(area)
elif option == "T":
  base = float(raw_input("Enter the base value: "))
  height = float(raw_input("Enter the height value: "))
  area = 0.5 * base * height
  print "The area of triangle is " + str(area)
else:
  print "Invalid entry"
print "Exiting...Bye"