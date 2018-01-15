i = [1,2,3]

s = 'hello world'

s[3:]
#the : means grap everything from index

s[:-1]
#grap everthing but the last one

s[::2]
#grap everything from the begining of everything and the end of everthing in steps of 2

s[::-1]
#reverse a string

# all of this is in syntax on 2.7
print 'string interpolation and template literals %s' %s
print 'flooting point %1.2f' %(12.123)
print('first %s, second %s, third %s' %('hi', 'hello', 1))

print('first: {x} second {y}'.format(x='bananas', y='yeah'))


####list is like arrays
my_list = ['A string',23,100.232,'o']
len(my_list)

first_col = [row[0] for row in matrix]


##DICTIONARY is like hash
#are not immutable and they can't be mapped but you can change their value
#can not have multiple keys being the exact same thing
my_dict = {'key1':'value1','key2':'value2'}
my_dict['key1']

#creating keys by assigment
# Create a new dictionary###
d = {}
# Create a new key through assignment
d['animal'] = 'Dog'
# Can do this with any object
d['answer'] = 42
#Show
d
{'animal': 'Dog', 'answer': 42}


## This are tuples
#they do have index and they can be mapped
# they are immutable meaning they cant be alter or change
t = (1,2,3)
t[0]

## This are FILES
my_file = open('test.txt')
my_file.read()
'Hello, this is a quick test file'
# But what happens if we try to read it again?
my_file.read()
''
# This happens because you can imagine the reading "cursor" is at the end of the file after having read it. So there is nothing left to read. We can reset the "cursor" like this:
# Seek to the start of file (index 0)
my_file.seek(0)
# Now read again
my_file.read()
'Hello, this is a quick test file'
# In order to not have to reset every time, we can also use the readlines method. Use caution with large files, since everything will be held in memory. We will learn how to iterate over large files later in the course.
# Readlines returns a list of the lines in the file.
my_file.readlines()
['Hello, this is a quick test file']


%%writefile new.txt
First line
Second line

Writing new.txt


for line in open('new.txt'):
    print(line)
First line
Second line

#SETs can be an unorder collection of unique elemnets can not repeat the unique key
#BOOLEANS

x = set()
# We add to sets with the add() method
x.add(1)
x
{1}
# Note the curly brackets. This does not indicate a dictionary! Although you can draw analogies as a set being a dictionary with only keys.
# mapping no sequence so cant sort
# Add a different element
x.add(2)
x
{1, 2}
# Try to add the same element
x.add(1)
x
{1, 2}
# Create a list with repeats
l = [1,1,2,2,3,4,5,6,1,1]
# Cast as set to get unique values
set(l)
{1, 2, 3, 4, 5, 6}

##comparasin operators

 <> same as !=
## Chaining operators
1 < 2 < 3

1<2 and 2<3

1==2 or 2<3

## Python statemns
    #js
    if (a>b){
    a = 2;
    b = 4;
}
    #python
    if a>b:
        a = 2
        b = 4

# Js
if (x)
    if(y)
        code-statement;
else
    another-code-statement;

# Python
if x:
    if y:
        code-statement
else:
    another-code-statement

# if,elif,else Statements
if case1:
    perform action1
elif case2:
    perform action2
else:
    perform action 3


x = False
if x:
    print 'x was True!'
else:
    print 'I will be printed in any case where x is not true'
# i will be printed in anycase where x ..


loc = 'Bank'

if loc == 'Auto Shop':
    print 'Welcome to the Auto Shop!'
elif loc == 'Bank':
    print 'Welcome to the bank!'
else:
    print "Where are you?"

## prints welcome to the bank ....

##For loops iterate through items

l = [1,2,3,4,5,6,7,8,9,10]

for num in l:
    print num
1
2
3
4
5
6
7
8
9
10

for num in l:
    if num % 2 == 0:
        print num
    else:
        print 'Odd number'

#adding numbers from the list
list_sum = 0

for num in l:
    list_sum = list_sum + num
print list_sum

## looping in a string
s = 'this is a string'
for letter in s:
    print letter

##looping through DICTIONARY

d = {'k1':1,'k2':2,'k3':3}

for k,v in d.items():
    print(k)
    print(v)
k1
1
k2
2
k3
3

##looping through Tuples
l = [(2,4),(6,8),(10,12)]

for tup in l:
    print tup
(2, 4)
(6, 8)
(10, 12)

# Now with unpacking!
for (t1,t2) in l:
    print t1
2
6
10

##while loop keeps performing until the condition is meet

# BREAKS: Breaks out of the current closest enclosing loop.
# CONTINUE: Goes to the top of the closest enclosing loop.
# PASS: Does nothing at all.

x = 0

while x <= 5:
    print('x is currently: ',x)
    x+=1

# x is currently:  0
# x is currently:  1
# x is currently:  2
# x is currently:  3
# x is currently:  4
# x is currently:  5

x = 0
while x < 4:
    print('x is currently:', x)
    x+=1
else:
    print('All done!')

# continuing
x = 0
while x < 10:
    print 'x is currently: ',x
    print ' x is still less than 10, adding 1 to x'
    x+=1
    if x ==3:
        print 'x==3'
    else:
        print 'continuing...'
        continue
#RANGE specify up to
range(start=0, stop, step=1)

x = range(11)
list(x)

range(x,y)

#LIST COMPRIHENTION
# I can do this or
l = []
for letter in 'word':
    l.append(letter)

print(l)
# same thing less code flatting out the for loop
l = [letter for letter in 'word']

# square a numbers
lst = [x**2 for x in range(0,11)]

# Check for even numbers in a range
lst = [x for x in range(11) if x % 2 == 0]

# Convert Celsius to Fahrenheit
celsius = [0,10,20.1,34.5]

fahrenheit = [ ((float(9)/5)*temp + 32) for temp in celsius ]

#Methods are essentially functions build in objects
#to get info about that method if i dont know it
help(count)


# functions are so we dont have to write the same code over and over
# The comment inside the function will be save to later reference
def name_of_function(arg1,arg2):
    '''
    This is where the function's Document String (doc-string) goes
    '''
name_of_function(1+2)

#writing basic function to great a person by their name
def greeting(name):
    print('Hello %s' %name)

greeting('Jose')

#return is a result of usually a function that can be stored as a variable
return

# finding a prime
def is_prime(num):
    for numero in range(2,num):
        if  num % numero == 0:
            print('Not a prime')
            break
    else:
        print('This is a prime!')

is_prime(18)

#using lambda
#1
def square(num):
    result = num**2
    return result

#2
def square(num):
    return num**2

#3
def square(num): return num**2

#4 lambda
square = lambda num: num**2

# name/item or object/ and what you want to do to that object


#checking if number are even
even = lambda x: x%2==0

#geting the first index of a string
first = lambda s: s[0]

#reversing a string
rev = lambda s: s[::-1]

#add 2 numbers
adder = lambda x,y : x+y

###NESTED STATEMENTS & SCOPE
# L: Local — Names assigned in any way within a function (def or lambda)), and not declared global in that function.
#
# E: Enclosing function locals — Name in the local scope of any and all enclosing functions (def or lambda), from inner to outer.
#
# G: Global (module) — Names assigned at the top-level of a module file, or declared global in a def within the file.
#
# B: Built-in (Python) — Names preassigned in the built-in names module : open,range,SyntaxError,...

#OBJECTS

class Dog(object):

    # Class Object Attribute
    species = 'mammal' # basically all the no matter what name or breed they will all be a mammal orrr something that is true for any instance of the class

    def __init__(self,breed,name): # this is the method
        self.breed = breed  # value is pass through class instanciation
        self.name = name

sam = Dog('Lab','Sam')  #  sam is an instance of the Dog object type and it has 2 Attributes

sam.name
'Sam'
# Note that the Class Object Attribute is defined outside of any methods in the class. Also by convention, we place them first before the init.
sam.species
'mammal'

#class circle

class Circle(object):
    pi = 3.14

    # Circle get instantiated with a radius (default is 1)
    def __init__(self, radius=1):
        self.radius = radius

    # Area method calculates the area. Note the use of self.
    def area(self):
        return (self.radius**2) * Circle.pi

    def perimeter(self):
        return 2 * (self.radius) * (Circle.pi)

    #c8 = Circle(radius = 100)
    #c8.perimeter()
    628.0

# string fucntions
#method                 True if
str.isalnum()	String consists of only alphanumeric characters (no symbols)
str.isalpha()	String consists of only alphabetic characters (no symbols)
str.islower()	String’s alphabetic characters are all lower case
str.isnumeric()	String consists of only numeric characters
str.isspace()	String consists of only whitespace characters
str.istitle()	String is in title case
str.isupper()	String’s alphabetic characters are all upper case
