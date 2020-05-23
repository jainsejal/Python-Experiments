# program that gives 12.0 as int instead of float 
import math 
def is_int(x):
  num = abs(x)
  num1 = math.floor(num)
  if (num1-num == 0):
    return True
  else:
    return False
	
print is_int(12.0)	