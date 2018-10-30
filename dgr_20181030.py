Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> fhand = open("text.txt","r")
>>> print(fhand)
<open file 'text.txt', mode 'r' at 0x7f1e8c6108a0>
>>> fhand = open("stuff.txt","r")

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    fhand = open("stuff.txt","r")
IOError: [Errno 2] No such file or directory: 'stuff.txt'
>>> stuff = "Hello\nWorld!"
>>> stuff
'Hello\nWorld!'
>>> print(stuff)
Hello
World!
>>> stuff = "X\nY"
>>> print(stuff)
X
Y
>>> len(stuff)
3
>>> xfile = open("text.txt")
>>> for cheese in xfile:
	print (cheese)

	


>>> 
>>> 
>>> for cheese in xfile:
	print (cheese)

	
>>> fhand = open("text.txt")
>>> count = 0
>>> for line in fhand:
	count = count +1

	
>>> print("Line Count", count)
('Line Count', 1)
>>> fhand = open("mbox-short.txt")

Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    fhand = open("mbox-short.txt")
IOError: [Errno 2] No such file or directory: 'mbox-short.txt'
>>> fhand = open("text-short.txt")

Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    fhand = open("text-short.txt")
IOError: [Errno 2] No such file or directory: 'text-short.txt'
>>> fhand = open("text-short.txt")

Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    fhand = open("text-short.txt")
IOError: [Errno 2] No such file or directory: 'text-short.txt'
>>> fhand = open("text-short.txt")

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    fhand = open("text-short.txt")
IOError: [Errno 2] No such file or directory: 'text-short.txt'
>>> fhand = open('mbox-short.txt")
	     
SyntaxError: EOL while scanning string literal
>>> fhand = open('mbox-short.txt')
>>> inp = fhand.read()
>>> print(len(imp))

Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print(len(imp))
NameError: name 'imp' is not defined
>>> print(len(inp))
29
>>> print(inp[:20])
123 un tu esi tiri b
>>> fhand = open('mbox-short.txt')
>>> for line in fhand:
	if line.start
	
SyntaxError: invalid syntax
>>> for line in fhand:
	if line.startwith('From:') :
		print(line)

		

Traceback (most recent call last):
  File "<pyshell#38>", line 2, in <module>
    if line.startwith('From:') :
AttributeError: 'str' object has no attribute 'startwith'
>>> fhand = open('mbox-short.txt')
>>> for line in fhand:
	if line.startswith('From:') :
		print(line)

		
>>> fhand = open('mbox-short.txt')
>>> for line in fhand:
	line = line.rstrip()
	if line.startswith('From:') :
		print(line)

		
>>> fhand = open('mbox-short.txt')
>>> for line in fhand:
	line = line.rstrip()
	if not line.startswith('From:') :
		continue
	print(line)

	
>>> fhand = open('mbox-short.txt')
>>> for line in fhand:
	line = line.rstrip()
	if not line.startswith('From:') :
		continue
	print(line)

	
From:
>>> fhand = open('mbox-short.txt')
>>> for line in fhand:
	line = line.rstrip()
	if not '@uct.ac.za' in line :
		continue
	print(line)

	
stephen.marquard@uct.ac.za
stephen.marquard@uct.ac.za
>>> fname = raw_input('Enter the file name:')
Enter the file name:mbox-short.txt
>>> fhand = open(fname)
>>> count = 0
>>> for line in fhand:
	if line.startswith("Subject:") :
		count = count + 1
	print("There were", count, "subject line in", fname)

	
('There were', 0, 'subject line in', 'mbox-short.txt')
('There were', 0, 'subject line in', 'mbox-short.txt')
('There were', 0, 'subject line in', 'mbox-short.txt')
('There were', 0, 'subject line in', 'mbox-short.txt')
('There were', 0, 'subject line in', 'mbox-short.txt')
('There were', 0, 'subject line in', 'mbox-short.txt')
('There were', 0, 'subject line in', 'mbox-short.txt')
('There were', 0, 'subject line in', 'mbox-short.txt')
('There were', 0, 'subject line in', 'mbox-short.txt')
('There were', 0, 'subject line in', 'mbox-short.txt')
('There were', 0, 'subject line in', 'mbox-short.txt')
('There were', 0, 'subject line in', 'mbox-short.txt')
('There were', 0, 'subject line in', 'mbox-short.txt')
('There were', 0, 'subject line in', 'mbox-short.txt')
('There were', 0, 'subject line in', 'mbox-short.txt')
('There were', 0, 'subject line in', 'mbox-short.txt')
('There were', 0, 'subject line in', 'mbox-short.txt')
('There were', 0, 'subject line in', 'mbox-short.txt')
('There were', 0, 'subject line in', 'mbox-short.txt')
('There were', 0, 'subject line in', 'mbox-short.txt')
('There were', 0, 'subject line in', 'mbox-short.txt')
('There were', 0, 'subject line in', 'mbox-short.txt')
('There were', 0, 'subject line in', 'mbox-short.txt')
('There were', 0, 'subject line in', 'mbox-short.txt')
('There were', 0, 'subject line in', 'mbox-short.txt')
('There were', 0, 'subject line in', 'mbox-short.txt')
('There were', 0, 'subject line in', 'mbox-short.txt')
('There were', 0, 'subject line in', 'mbox-short.txt')
('There were', 0, 'subject line in', 'mbox-short.txt')
('There were', 1, 'subject line in', 'mbox-short.txt')
('There were', 1, 'subject line in', 'mbox-short.txt')
('There were', 1, 'subject line in', 'mbox-short.txt')
('There were', 1, 'subject line in', 'mbox-short.txt')
('There were', 1, 'subject line in', 'mbox-short.txt')
('There were', 1, 'subject line in', 'mbox-short.txt')
('There were', 1, 'subject line in', 'mbox-short.txt')
('There were', 1, 'subject line in', 'mbox-short.txt')
('There were', 1, 'subject line in', 'mbox-short.txt')
('There were', 1, 'subject line in', 'mbox-short.txt')
('There were', 1, 'subject line in', 'mbox-short.txt')
('There were', 1, 'subject line in', 'mbox-short.txt')
('There were', 1, 'subject line in', 'mbox-short.txt')
('There were', 1, 'subject line in', 'mbox-short.txt')
('There were', 1, 'subject line in', 'mbox-short.txt')
('There were', 1, 'subject line in', 'mbox-short.txt')
('There were', 1, 'subject line in', 'mbox-short.txt')
('There were', 1, 'subject line in', 'mbox-short.txt')
('There were', 1, 'subject line in', 'mbox-short.txt')
('There were', 1, 'subject line in', 'mbox-short.txt')
>>> fname = raw_input('Enter the file name:')
Enter the file name:
>>> 
