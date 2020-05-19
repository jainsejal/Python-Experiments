# putting dict into list and accessing it
lloyd = {
  "name": "Lloyd",
  "homework": [ 90.0, 97.0, 75.0, 92.0 ],
  "quizzes": [ 88.0, 40.0, 94.0 ],
  "tests": [ 75.0, 90.0 ]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

students = [ lloyd, alice, tyler ]
for items in students:
  print items["name"]
  print items["homework"]
  print items["quizzes"]
  print items["tests"]
  
  
o/p  
   Lloyd
[90.0, 97.0, 75.0, 92.0]
[88.0, 40.0, 94.0]
[75.0, 90.0]
Alice
[100.0, 92.0, 98.0, 100.0]
[82.0, 83.0, 91.0]
[89.0, 97.0]
Tyler
[0.0, 87.0, 75.0, 22.0]
[0.0, 75.0, 78.0]
[100.0, 100.0]