#calculator
print("enter the first number")
a = int(input())
print("enter the second number")
b = int(input())
c = str(input("operator"))
if (c=="+"):
 print("the addition ", a, "+", b, "is:", a + b)
elif(c=="-"):
  print("the subtraction ", a, "-", b, "is:", a - b)
elif (c=="*"):
 print("the multiplication ", a, "*", b, "is:", a * b)
elif (c=="%"):
 print("the module", a, "%", b, "is:", a % b)
elif(c=="/"):
 print("the division ", a, "/", b, "is:", a / b)
elif(c=="//"):
 print("the  ", a, "//", b, "is:", a // b)
elif(c=="**"):
 print("the times ", a, "**", b, "is:", a ** b)
else:
 print("invalid operation")
