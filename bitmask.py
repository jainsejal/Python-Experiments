#It should check to see if the fourth bit from the right is on.
def check_bit4(inp):
  mask = 0b1000
  desired = inp & mask
  if desired > 0:
    return "on"
  else:
    return "off"
  
print check_bit4(0b101101)

#whether third bit is on
num  = 0b1100
mask = 0b0100
desired = num & mask
if desired > 0:
  print "Bit was on"
  
# for OR wher 3rd bit is on and it is a mask
a = 0b10111011
mask = 0b100
desired = a | mask
print bin(desired)

#for XOR flipping the bits
a = 0b11101110
mask = 0b11111111
desi = a ^ mask
print bin(desi)

# XORing the number
def flip_bit(number,n):
  mask = (0b1 << (n-1))
  result = number ^ mask
  return bin(result)
print flip_bit(0b101, 10)