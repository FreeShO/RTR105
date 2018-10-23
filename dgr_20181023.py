Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> str1 = "Hello"
>>> str2 = "There"
>>> bob = str1 + str2
>>> print(bob)
HelloThere
>>> str3 = "123"
>>> str3 = str3 +1

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    str3 = str3 +1
TypeError: cannot concatenate 'str' and 'int' objects
>>> x = int(str3) + 1
>>> print (x)
124
>>> name = raw_input("Enter:")
Enter:Chuck
>>> print(name)
Chuck
>>> apple = raw_input("Enter:")
Enter:100
>>> x= apple -10

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    x= apple -10
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> x = int(apple) - 10
>>> print (x)
90
>>> fruit = "banana"
>>> letter = fruit [1]
>>> print (latter)

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print (latter)
NameError: name 'latter' is not defined
>>> print (letter)
a
>>> x=3
>>> w=fruit[x-1]
>>> print(w)
n
>>> zot = "abc"
>>> print (zot[5])

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print (zot[5])
IndexError: string index out of range
>>> print (zot[2])
c
>>> print (zot[1])
b
>>> fruit = "banana"
>>> print (len(fruit))
6
>>> fruit = "banana"
>>> x= len(fruit)
>>> print (x)
6
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index]
	print(index, latter)
	index = index +1

	

Traceback (most recent call last):
  File "<pyshell#35>", line 3, in <module>
    print(index, latter)
NameError: name 'latter' is not defined
>>> while index < len(fruit):
	letter = fruit[index]
	print(index, letter)
	index = index +1

	
(0, 'b')
(1, 'a')
(2, 'n')
(3, 'a')
(4, 'n')
(5, 'a')
>>> for letter in fruit:
	print(letter)

	
b
a
n
a
n
a
>>> index = 0
>>> while index < len(fruit) :
	letter = fruit[index]
	print(letter)
	index = index +1

	
b
a
n
a
n
a
>>> word = "banana"
>>> count = 0
>>> for letter == "a":
	
SyntaxError: invalid syntax
>>> for letter == "a":
	
SyntaxError: invalid syntax
>>> for letter in word :
	if letter == "a" :
		count = count +1
	print (count)

	
0
1
1
2
2
3
>>> s= "Monty Python"
>>> print (s[6:7])
P
>>> print (s[0:4])
Mont
>>> print (s[6:7])
P
>>> print (s[6:20])
Python
>>> print (s[:2])
Mo
>>> print (s[8:])
thon
>>> print (s[:])
Monty Python
>>> a = "Hello"
>>> b = a + "There"
>>> print (b)
HelloThere
>>> c= a + "" + "There"
>>> print (c)
HelloThere
>>> fruit = "banana"
>>> "n" in fruit
True
>>> "m" in fruit
False
>>> "nan"in fruit
True
>>> if "a" in fruit :
	print ("Found it!")

	
Found it!
>>> if word == 'banana':
	print('All right, bananas.')

All right, bananas.
>>> if word < 'banana' :
	print('Your word,'+ word +", comes before banana.')
elif word > 'banana' :
	print('Your word,'+ word +', comes after banana.')
else:
	print('All right, bananas.')
	      
SyntaxError: EOL while scanning string literal
>>> if word < 'banana' :
	print('Your word,'+ word +", comes before banana.")
elif word > 'banana' :
	print('Your word,'+ word +', comes after banana.')
else:
	print('All right, bananas.')

	
All right, bananas.
>>> greet = "Hello Bob"
>>> zap = greet.lower()
>>> print(zap)
hello bob
>>> print(greet)
Hello Bob
>>> print ("Hi There".lower())
hi there
>>> stuff = "Hello world"
>>> type(stuff)
<type 'str'>
>>> dir(stuf)

Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    dir(stuf)
NameError: name 'stuf' is not defined
>>> dir(stuff)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 
>>> stuff.upper()
'HELLO WORLD'
>>> stuff.lowwer()

Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    stuff.lowwer()
AttributeError: 'str' object has no attribute 'lowwer'
>>> stuff.lower()
'hello world'
>>> fruit = "banana"
>>> pos = fruit.find("na")
>>> print (pos)
2
>>> aa=fruit.find("z")
>>> print(aa)
-1
>>> greet = "Hello Bob"
>>> nnn= greet.upper()
>>> print(nnn)
HELLO BOB
>>> www = greet.lower()
>>> print(www)
hello bob
>>> 
