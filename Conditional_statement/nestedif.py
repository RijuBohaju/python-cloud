age = int(input("Enter your age"))
if (age < 0):
  print("invalid age")
elif (age > 0):
  if (age < 10):
    print("age lies in between 0-10")
  elif (age > 10 and age < 20):
    print("Teenagers")
  else:
   print("Adult")
else:
  print("Age is zerp")