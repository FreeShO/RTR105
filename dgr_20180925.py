Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> vars ()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> input ("Cienījamais lietotāj, lūdzu, ievadi vienu skatili: ")
Cienījamais lietotāj, lūdzu, ievadi vienu skatili: 10
10
>>> vars ()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> mans_mainigais = input("Cienījamais lietotāj, lūdzu, ievadi vienu skatili: ")
Cienījamais lietotāj, lūdzu, ievadi vienu skatili: 10
>>> vars ()
{'__builtins__': <module '__builtin__' (built-in)>, 'mans_mainigais': 10, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> mans_mainigais
10
>>> mans_mainigais = input("Cienījamais lietotāj, lūdzu, ievadi vienu skatili: ")
Cienījamais lietotāj, lūdzu, ievadi vienu skatili: 20
>>> vars ()
{'__builtins__': <module '__builtin__' (built-in)>, 'mans_mainigais': 20, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> type(mans_mainigais)
<type 'int'>
>>> 
>>> 
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, 'mans_mainigais': 20, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skatili: 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skatili: 8

=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skatili: 7
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/test_1_20180925.py', 'mans_mainigais': 7, '__package__': None, 'x': 49, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skatili: 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skatili: 41
mans_mainigais =
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skatili: 156
mans_mainigais = 156
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skatili: 12
mans_mainigais = 12
Respektīvi, Tu esi ievadījis skaitli: 12
vēl atmiņā tagad ir mainīgais x = 144
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skatili: 8.6549
mans_mainigais =      8.655
Respektīvi, Tu esi ievadījis skaitli:     8.6549
vēl atmiņā tagad ir mainīgais x =      74.9072940
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi daļskaitli: 7.8
mans_mainigais =      7.800
Respektīvi, Tu esi ievadījis skaitli:     7.8000
vēl atmiņā tagad ir mainīgais x =      60.8400000
>>> 
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi daļskaitli: 8
mans_mainigais =      8.000
Respektīvi, Tu esi ievadījis skaitli:     8.0000
vēl atmiņā tagad ir mainīgais x =      64.0000000
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi daļskaitli: 9
mans_mainigais =      9.000
Respektīvi, Tu esi ievadījis skaitli:     9.0000
vēl atmiņā tagad ir mainīgais x =      81.0000000
>>> type()

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    type()
TypeError: type() takes 1 or 3 arguments
>>> type ()

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    type ()
TypeError: type() takes 1 or 3 arguments
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi daļskaitli: 12
mans_mainigais =     12.000
Respektīvi, Tu esi ievadījis skaitli:    12.0000
vēl atmiņā tagad ir mainīgais x =     144.0000000
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi simbolu rindu: asd

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 1, in <module>
    mans_mainigais = 1. * raw_input("Cienījamais lietotāj, lūdzu, ievadi simbolu rindu: ")
TypeError: can't multiply sequence by non-int of type 'float'
>>> 

