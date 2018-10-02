Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> print(123)
123
>>> print(98.6)
98.6
>>> print(Hello world)
SyntaxError: invalid syntax
>>> print('Hello world')
Hello world
>>> print(class)
SyntaxError: invalid syntax
>>> print("class")
class
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> x=12.2
>>> y=14
>>> vars ()
{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 12.2, 'y': 14, '__name__': '__main__', '__doc__': None}
>>> x=100
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 100, 'y': 14, '__name__': '__main__', '__doc__': None}
>>> spam

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    spam
NameError: name 'spam' is not defined
>>> eggs

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    eggs
NameError: name 'eggs' is not defined
>>> _spam

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    _spam
NameError: name '_spam' is not defined
>>> x1q3z9ocd = 35.0
>>> x1q3z9afd = 12.50
>>> x1q3p9afd = x1q3z9ocd * x1q3z9afd
>>> print(x1q3p9afd)
437.5
>>> a = 35.0
>>> b = 12.50
>>> c = a * b
>>> print(c)
437.5
>>> hours = 35.0
>>> rate = 12.50
>>> pay = hours * rate
>>> print(pay)
437.5
>>> vars()
{'a': 35.0, 'c': 437.5, 'b': 12.5, '__builtins__': <module '__builtin__' (built-in)>, 'pay': 437.5, '__package__': None, 'hours': 35.0, 'x1q3z9afd': 12.5, 'rate': 12.5, 'x1q3p9afd': 437.5, 'x': 100, 'y': 14, '__name__': '__main__', '__doc__': None, 'x1q3z9ocd': 35.0}
>>> x=2
>>> x=x+2
>>> print(x)
4
>>> x=3.9*x*(1-x)
>>> print(x)
-46.8
>>> x=0.6
>>> x=3.9*x*(1-x)
>>> print(x)
0.936
>>> vars()
{'a': 35.0, 'c': 437.5, 'b': 12.5, '__builtins__': <module '__builtin__' (built-in)>, 'pay': 437.5, '__package__': None, 'hours': 35.0, 'x1q3z9afd': 12.5, 'rate': 12.5, 'x1q3p9afd': 437.5, 'x': 0.9359999999999999, 'y': 14, '__name__': '__main__', '__doc__': None, 'x1q3z9ocd': 35.0}
>>> xx=2
>>> xx=xx+2
>>> print(xx)
4
>>> yy=440*12
>>> print(yy)
5280
>>> zz=yy/1000
>>> print(zz)
5
>>> jj = 23
>>> kk=jj%5
>>> print (kk)
3
>>> print(4 ** 3)
64
>>> x=1+2*3-4/5**6
>>> print (x)
7
>>> x=1+2**3/4*5
>>> print (x)
11
>>> ddd=1+4
>>> print(ddd)
5
>>> eee = 'hello ' + 'there'
>>> print (eee)
hello there
>>> eee= eee+1

Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    eee= eee+1
TypeError: cannot concatenate 'str' and 'int' objects
>>> type (eee)
<type 'str'>
>>> type ("hello")
<type 'str'>
>>> type (1)
<type 'int'>
>>> xx=1
>>> type (xx)
<type 'int'>
>>> temp = 98.6
>>> type (temp)
<type 'float'>
>>> type (1)
<type 'int'>
>>> type (1.0)
<type 'float'>
>>> 
print(float(99) + 100)
199.0
>>> i=42
>>> print(42)
42
>>> type (i)
<type 'int'>
>>> f=float(i)
>>> print(f)
42.0
>>> type(f)
<type 'float'>
>>> print(10/2)
5
>>> print(9/2)
4
>>> print(99/100)
0
>>> print (10.0/2.0)
5.0
>>> print(99.0/100.0)
0.99
>>> sval='123'
>>> type(sval)
<type 'str'>
>>> type(sval+1)

Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    type(sval+1)
TypeError: cannot concatenate 'str' and 'int' objects
>>> ival = int(sval)
>>> type(ival)
<type 'int'>
>>> type(ival+1)
<type 'int'>
>>> print(ival +1)
124
>>> nsv='hello bob'
>>> niv=int(nsv)

Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    niv=int(nsv)
ValueError: invalid literal for int() with base 10: 'hello bob'
>>> nam=input('Who are you?')
Who are you?

Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    nam=input('Who are you?')
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> nam=input('Who are you?')
Who are you? Me

Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    nam=input('Who are you?')
  File "<string>", line 1, in <module>
NameError: name 'Me' is not defined
>>> print('Welcome', nam)

Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    print('Welcome', nam)
NameError: name 'nam' is not defined
>>> nam

Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    nam
NameError: name 'nam' is not defined
>>> nam=input('Who are you?')
Who are you?print('Welcome', nam)

Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    nam=input('Who are you?')
  File "<string>", line 1
    print('Welcome', nam)
        ^
SyntaxError: invalid syntax
>>> print('Welcome', nam)

Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    print('Welcome', nam)
NameError: name 'nam' is not defined
>>> nam=input('Who are you?')
Who are you?ooooo

Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    nam=input('Who are you?')
  File "<string>", line 1, in <module>
NameError: name 'ooooo' is not defined
>>> inp=input('Europe floor?')
Europe floor?0
>>> usf=int(inp) +1
>>> print('US floor',usf)
('US floor', 1)
>>> name = 
input
('Enter file:')
SyntaxError: invalid syntax
>>> name =
input
('Enter file:')name =
input
('Enter file:')
SyntaxError: invalid syntax
>>> hours=35
>>> rate=2.75
>>> pay=hours*rate
>>> print(pay)
96.25
>>> vars()
{'x1q3p9afd': 437.5, 'x1q3z9afd': 12.5, 'inp': 0, 'xx': 1, 'zz': 5, 'nsv': 'hello bob', 'usf': 1, 'pay': 96.25, 'sval': '123', '__package__': None, '__doc__': None, 'ddd': 5, '__builtins__': <module '__builtin__' (built-in)>, 'yy': 5280, 'eee': 'hello there', 'jj': 23, 'x1q3z9ocd': 35.0, '__name__': '__main__', 'a': 35.0, 'hours': 35, 'c': 437.5, 'b': 12.5, 'temp': 98.6, 'f': 42.0, 'kk': 3, 'rate': 2.75, 'i': 42, 'y': 14, 'x': 11, 'ival': 123}
>>> file
