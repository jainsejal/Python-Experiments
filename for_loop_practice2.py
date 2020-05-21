# For loop revision
hobbies = []
# Add your code below!
for item in range(3):
  user = raw_input("Your hobby: ")
  hobbies.append(str(user))
  print hobbies
 
""" o/P
Your hobby: drawing
['drawing']
Your hobby: running
['drawing', 'running']
Your hobby: climbing
['drawing', 'running', 'climbing']"""