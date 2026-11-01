# name = "ram"
# print(name[0])
# print("\nlet's use for loop")
# for character in name:
#   print(character)
# car = ["honda", "bmw", "mustang"]
# print(car[1])

name = "Radhe, Shyam"
print(name[0:5])  #including zero but not 5
print(name[:5])
print(name[0:-3])  #length of name - 3
print(name[-3:-2])  # length of name -3 to length of name-2 (9to10)

#length of a string= we can measure length of astring using len()
print(len(name))

name = "mango"
len1 = len(name)
print("Mango is a", len1, "letter word")

#String methods
#Strings are imutable
a = "Riju!!!!"
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
b = "!!! Python !!!"
print(b.strip("!"))  #remove trailing characters from startin to last
print(b.rstrip("!"))  #remove ending trailing characters

print(a.replace("Riju", "Rajju"))
c = "ram"
print(c.replace("ram", "Shyam"))

#split()
print(b.split(" "))  #makes list according to the space given in a string

#Capitalize()= capitalize the first letter of a sentence
print(c.capitalize())
intro = "introduction to pYthon"  #autocorrects all the error= only turns first letter into capitalize but it will convert left string in lowercase
print(intro.capitalize())

#center()=this method align the string into center as per the parameters given by the user
print(intro.center(50))
print(len(intro))
print(len(intro.center(50)))

#count() method=returns the number of times th given value has occured in astring
print(intro.count("n"))
print("The no. of n is:",intro.count("n"))

#endswith() method=checks if the  string ends with given value. if yes return true else false
print(intro.endswith("n"))
#we can also check for a value in between the string by providing start and end index position
print(intro.endswith("to",13,15))

#startswith()
print(intro.startswith("intro"))

#find() method=search th first occurence of the given value and return index where it is present if not present then it returns -1
print(intro.find("to"))

#index()= same as find but it gives error if the given string is not found
#print(itro.index("too"))

#isalnum()=returns trus if entire string consist of A-Z a-z 0-9
str="hElloMike9"
print(str.isalnum())

#isalpha=A-Z a-z
print(str.isalpha())

#islower()=checks if the string consists of lowercase only
print(str.islower())
#isupper()

#isprintable()=if all the characters in string is printable then return true
print(str.isprintable())
no="\nhello"
print(no.isprintable())

#isspace()=if string consists of whitespace only return true
sp="  "
print(sp.isspace())

 #istitle()= if first letter if each word is capitalized
cp="Hello To All"
print(cp.istitle())

#swapcase()= swap to uppercase if the string is in lowercase or viceversa
swap="Henry"
print(swap.swapcase())

#title()=convert the string into title
t="hi everyone"
print(t.title())
