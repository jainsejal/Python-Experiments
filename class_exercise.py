#practice session for class
class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg
   
  def display_car(self):
    print "This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg))
    
  def drive_car(self):
    self.condition = "used"

class ElectricCar(Car):
  def __init__(self, model, color, mpg, battery_type):
    self.model = model
    self.color = color
    self.mpg   = mpg
    self.battery_type = battery_type
  def drive_car(self):
    self.condition = "like new"

my_car = ElectricCar("DeLorean", "silver", 88, "molten salt")
#OR	
my_car = Car("DeLorean", "silver", 88)
#first printing the original value "new"
print my_car.condition
# now call the method to print the new modified value "used"
my_car.drive_car()
print my_car.condition
#print my_car.model
#print my_car.color
#print my_car.mpg
#my_car.display_car()

#prints original value "new"
print my_car.condition
#prints new value "like new"
my_car.drive_car()
print my_car.condition
