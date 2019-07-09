

print("teste")

x = 1
if x == 1:
    print("x is 1")
    print("outro")
else:
    print ("else")


print ('fora')

myInt = 3
print (myInt)

myFloat = 7.0
print (myFloat)
myFloat = float("6.4")
print (myFloat-1)
print (5/2)

print (int(5/2))

a, b = 1, 2
print (a, b)
myFloat = 100 / 3
"""
sdfasdf
aasdfasdf

"""

print ("Numero : %.2f" % myFloat)

a = 11.0
a /= 3
print (a)
if 5 > 2:
 print("Five is greater than two!")

x = y = z = "Orange"
x = 1
z = 2j
print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))


x = 3+5j
y = complex(1)
z = float(5)

print(x)
print(y)
print(type(z))

import random
print(random.randrange(1,10))

a = """sdfsdkfalsdkfasld~fa
asdfasdf asdf asdfsad """
print(a)
print(a[0])
print(a[0:10])

print(a.strip())
print (len(a))

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

thislist = ["apple", "banana", "cherry"]
other = thislist
other[0] = 'a'
for x in thislist:
    print(x)

meuSet = {"a", "b", "c"}
meuSet.add('d')
print(meuSet)

print ("a" in meuSet)
meuSet.update(["orange", "mango", "grapes"])
for x in meuSet:
    print(x)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

for x in thisdict:
  print(x  + ' = ' + str(thisdict[x]))

a = 1
b = 2

print("A") if a > b else print("B")

for x in range(2, 30, 3):
  print(x)

for x in range(6):
  print(x)
else:
  print("Finally finished!")

volume = 25

if volume < 20 or volume > 80:
  volume = 50
  print("Bem melhor!")

def oi():
  print("Olá")
  print("Tudo bem?")

oi()