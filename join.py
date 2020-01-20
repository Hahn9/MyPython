Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s = """line1\nline2\nline3\n"""
      print s
SyntaxError: multiple statements found while compiling a single statement
>>> s='hello,world'
>>> print s
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(s)?
>>> s='hello,world'
>>> print(s)
hello,world
>>> s='abcdefg'
>>> s[0:]
'abcdefg'
>>> s[-1]
'g'
>>> s[0;-1]
SyntaxError: invalid syntax
>>> s[0:-1]
'abcdef'
>>> s[-1:-1]
''
>>> s = """line1\nline2\nline3\n"""
>>> print(s)
line1
line2
line3

>>> s = "line1\nline2\nline3\n"
>>> print(s)
line1
line2
line3

>>> int(input("enter a real number"))
enter a real number
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    int(input("enter a real number"))
ValueError: invalid literal for int() with base 10: ''
>>> a = int (input("enter a real number"))
enter a real number
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a = int (input("enter a real number"))
ValueError: invalid literal for int() with base 10: ''
>>> s="0123456"
>>> s[0:]
'0123456'
>>> s[0]
'0'
>>> s[2]
'2'
>>> s[s[0]:s[2]]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    s[s[0]:s[2]]
TypeError: slice indices must be integers or None or have an __index__ method
>>> s[int(s[0]):int(s[2])]
'01'
>>> s="abcdefg"
>>> x=2
>>> s[x]
'c'
>>> s[x,x+1]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    s[x,x+1]
TypeError: string indices must be integers
>>> s[x]
'c'
>>> s[x,x+1]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    s[x,x+1]
TypeError: string indices must be integers
>>> s[x]
'c'
>>> s[2,3]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    s[2,3]
TypeError: string indices must be integers
>>> s[x,abs(x-2)]
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    s[x,abs(x-2)]
TypeError: string indices must be integers
>>> abs(-1)
1
>>> s="abcdefg"
>>> s[0]
'a'
>>> s="bcdefg"
>>> s[0]
'b'
>>> s[0]="a"
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    s[0]="a"
TypeError: 'str' object does not support item assignment
>>> s[0]
'b'
>>> s="a"+s[0:]
>>> s[0]
'a'
>>> "ac" in s
False
>>> "abc" in s
True
>>> stringname.
SyntaxError: invalid syntax
>>> s.upper()
'ABCDEFG'
>>> s.isupper
<built-in method isupper of str object at 0x0000000002D84998>
>>> s.find()
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    s.find()
TypeError: find() takes at least 1 argument (0 given)
>>> s.lower()
'abcdefg'
>>> s.isupper()
False
>>> s.islower()
True
>>> s.find()
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    s.find()
TypeError: find() takes at least 1 argument (0 given)
>>> s="   abc def"
>>> s.strip('')
'   abc def'
>>> s.strip(" ")
'abc def'
>>> s.strip("")
'   abc def'
>>> s="xxxabc xxxdef"
>>> s.strip("x")
'abc xxxdef'
>>> s="abcde"
>>> s.find("b")
1
>>> s.find("ec")
-1
>>> s.find("da")
-1
>>> s="abcdef"
>>> s.find("da")
-1
>>> print "This string has a %d in it" % 4
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("This string has a %d in it" % 4)?
>>> print "This string has a %d in it"%4
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("This string has a %d in it"%4)?
>>> print ("This string has a %d in it" % 4)
This string has a 4 in it
>>> s="abcd"
>>> "a" in s
True
>>> "cd\n" in s
False
>>> "cd" in s
True
>>> s="abc"
>>> upper(s)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    upper(s)
NameError: name 'upper' is not defined

>>> s.upper(s)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    s.upper(s)
TypeError: upper() takes no arguments (1 given)
>>> s.upper()
'ABC'
>>> s="ABC"
>>> upper(s)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    upper(s)
NameError: name 'upper' is not defined
>>> s.isupper
<built-in method isupper of str object at 0x0000000001D6DE68>
>>> s.isupper()
True
>>> upper(s)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    upper(s)
NameError: name 'upper' is not defined
>>> s.isupper()
True
>>> upper(s)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    upper(s)
NameError: name 'upper' is not defined
>>> print "你好，世界"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("你好，世界")?
>>> "你好，世界"
KeyboardInterrupt
>>> s="你好，世界"
>>> print (s)
你好，世界
>>> print("你好，世界")
你好，世界
>>> 
KeyboardInterrupt
>>> print("hello");print("world")
hello
world
>>> days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
>>> print (days)
['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
>>> s="abcd"
>>> s[0]
'a'
>>> s[-0]
'a'
>>> s[-0]
'a'
>>> s="hello,world"
>>> s[4,7]
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    s[4,7]
TypeError: string indices must be integers
>>> s[4:7]
'o,w'
>>> s[2]
'l'
>>> s[1,2]
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    s[1,2]
TypeError: string indices must be integers
>>> s="abcdef"
>>> x=2
>>> s[x]
'c'
>>> s[x,x+1]
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    s[x,x+1]
TypeError: string indices must be integers
>>> len([1,2,3,4,5])
5
>>> [1,2]+[5,6,8]
[1, 2, 5, 6, 8]
>>> ["HI!"]*8
['HI!', 'HI!', 'HI!', 'HI!', 'HI!', 'HI!', 'HI!', 'HI!']
>>> L=[1,2,3,4,5]
>>> L[2]
3
>>> max(L)
5
>>> min(L)
1
>>> list.append(10)
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    list.append(10)
TypeError: descriptor 'append' requires a 'list' object but received a 'int'
>>> list.append("10")
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    list.append("10")
TypeError: descriptor 'append' requires a 'list' object but received a 'str'
>>> list.append(list[10,11])
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    list.append(list[10,11])
TypeError: 'type' object is not subscriptable
>>> tup(1,2,3,4,5)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    tup(1,2,3,4,5)
NameError: name 'tup' is not defined
>>> tup=(1,2,3,4,5)
>>> tup[0]
1
>>> tup=(0,3,6,7,9,4)
>>> min(tup)
0
>>> max(tup)
9
>>> mid(tup)
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    mid(tup)
NameError: name 'mid' is not defined
>>> cmp(tup2,tup4)
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    cmp(tup2,tup4)
NameError: name 'cmp' is not defined
>>> len(tup)
6
>>> tuple(seq)
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    tuple(seq)
NameError: name 'seq' is not defined
>>> x=[1,2,3,4]
>>> x.reverse()
>>> print(x)
[4, 3, 2, 1]
>>> x.pop()
1
>>> x
[4, 3, 2]
>>> x=[1,2,3,4,5]
>>> x
[1, 2, 3, 4, 5]
>>> x.insert(1,5)
>>> x
[1, 5, 2, 3, 4, 5]
>>> x.insert(1,5)
>>> x
[1, 5, 5, 2, 3, 4, 5]
>>> x.insert(5,9)
>>> x
[1, 5, 5, 2, 3, 9, 4, 5]
>>> x.append(6)
>>> x
[1, 5, 5, 2, 3, 9, 4, 5, 6]
>>> x.count(5)
3
>>> x.reverse()
>>> 
>>> x
[6, 5, 4, 9, 3, 2, 5, 5, 1]
>>> x
[6, 5, 4, 9, 3, 2, 5, 5, 1]
>>> x.remove(5)
>>> x
[6, 4, 9, 3, 2, 5, 5, 1]
>>> x.remove(5)
>>> x
[6, 4, 9, 3, 2, 5, 1]
>>> x=[a,b,c,d]
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    x=[a,b,c,d]
NameError: name 'a' is not defined
>>> a=1
>>> b=2
>>> c=3
>>> d=4
>>> x=[a,b,c,d]
>>> x
[1, 2, 3, 4]
>>> x=[]
>>> x
[]
>>> x.append(5)
>>> x
[5]
>>> x=[]
>>> x
[]
>>> x.count()
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    x.count()
TypeError: count() takes exactly one argument (0 given)
>>> x.count(1)
0
>>> if '':
	print "False"
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("False")?
>>> if '':
	print ("False")
    else:
	    
SyntaxError: unindent does not match any outer indentation level
>>> if '':
	print"True"
	
SyntaxError: invalid syntax
>>> if '' :
print "false"
else:
print "true“
SyntaxError: expected an indented block
>>> if '' :
           print "false"
else:
           print "true“
           
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("false")?
>>> if '' :
           print (false)
else:
           print (true)

           
Traceback (most recent call last):
  File "<pyshell#171>", line 4, in <module>
    print (true)
NameError: name 'true' is not defined
>>> if '' :
           print ("false")
else:
           print ("true“)
		  
SyntaxError: EOL while scanning string literal
>>> x=[1,2,3,4,5]
		  
>>> x[4]=9
		  
>>> x
		  
[1, 2, 3, 4, 9]
>>> x[2]=8
		  
>>> x
		  
[1, 2, 8, 4, 9]
>>> 
KeyboardInterrupt
>>> 
		  
>>> s=[1,2,3,4,5]
		  
>>> s
		  
[1, 2, 3, 4, 5]
>>> s.join(list)
		  
Traceback (most recent call last):
  File "<pyshell#181>", line 1, in <module>
    s.join(list)
AttributeError: 'list' object has no attribute 'join'
>>> L=[1,2,3,4,5]
		  
>>> L
		  
[1, 2, 3, 4, 5]
>>> s.join(L)
		  
Traceback (most recent call last):
  File "<pyshell#184>", line 1, in <module>
    s.join(L)
AttributeError: 'list' object has no attribute 'join'
>>> l=["one","two","three"]
		  
>>> l
		  
['one', 'two', 'three']
>>> ",",join
		  
Traceback (most recent call last):
  File "<pyshell#187>", line 1, in <module>
    ",",join
NameError: name 'join' is not defined
>>> ",",join(l)
		  
Traceback (most recent call last):
  File "<pyshell#188>", line 1, in <module>
    ",",join(l)
NameError: name 'join' is not defined
>>> ",",join(l)
		  
Traceback (most recent call last):
  File "<pyshell#189>", line 1, in <module>
    ",",join(l)
NameError: name 'join' is not defined
>>> l=["one","two","three"]
		  
>>> l
		  
['one', 'two', 'three']
>>> ",,,",join(l)
		  
Traceback (most recent call last):
  File "<pyshell#192>", line 1, in <module>
    ",,,",join(l)
NameError: name 'join' is not defined
>>> 
