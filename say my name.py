#Say my name.py
Name = input("What is your name: ")
print("Let me guess your name is",Name,"am I right")
Question = input("Am I right: ")
Question2 = input("How many times may I print your name: ")
for x in range(int(Question2)):
  print(Name, end = " rules ")
