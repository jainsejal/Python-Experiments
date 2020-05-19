# Class definition
class Animal(object):
  """Makes cute animals."""
  is_alive = True
  health = "good"
  # For initializing our instance objects
  def __init__(self, name, age, is_hungry):
    self.name = name
    self.age = age
    self.is_hungry = is_hungry

# Note that self is only used in the __init__()
# function definition; we don't need to pass it
# to our instance objects.
  def description(self):
    print self.name
    print self.age

hippo = Animal("rino", 5)
hippo.description()
sloth = Animal("lazyass", 6)
ocelot = Animal("newbie", 4)
print hippo.health
print sloth.health
print ocelot.health
#--------------------------------------------------------------------------------------
zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)
print zebra.name, zebra.age, zebra.is_hungry
print giraffe.name, giraffe.age, giraffe.is_hungry
print panda.name, panda.age, panda.is_hungry