"""Guessing the number by adding the numbers coming in pair of dice """
from random import randint
from time import sleep
def get_user_guess():
  guess = int(raw_input("Guess a number: "))
  return guess
def roll_dice(number_of_sides):  
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = 2 * number_of_sides
  print "The maximum value is %d" % max_val
  guess = get_user_guess()
  if guess > max_val:
    print "Guess the number less or equal to maximum value"
  else:
    print "Rolling..."
    sleep(2)
    print "Value of first roll is %d" % first_roll
    sleep(1)
    print "Value of second roll is %d" % second_roll
    sleep(1)
    total_roll = first_roll + second_roll
    print "The total value is: %d" % total_roll
    print "Result..."
    sleep(1)
    if guess == total_roll:
      print "Hey Congrats. You are a winner!"
    else:
      print "Oops! Loser"
roll_dice(6)
      