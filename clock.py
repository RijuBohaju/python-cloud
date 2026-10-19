import time

timestamp = time.strftime('%H:%M:%S')
print("The time right now is", timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)

hours = int(time.strftime('%H'))

if hours >= 0 and hours <= 12:
  print("Good Morning Captain")
elif hours > 12 and hours < 17:
  print("Good Aternoon Captain")
elif hours > 17 and hours < 20:
  print("Good Evening Captain")
else:
  print("Good Night")