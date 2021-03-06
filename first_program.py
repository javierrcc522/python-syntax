i = [1,2,3]

s = 'hello world'

#SLICing a number
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
# The primary way in which tuples are different from lists is that they cannot be modified. This means that items cannot be added to or removed from tuples, and items cannot be replaced within tuples.

You can, however, concatenate 2 or more tuples to form a new tuple.
t = (1,2,3)
t[0]
# concating tuples
coral = ('blue coral', 'staghorn coral', 'pillar coral', 'elkhorn coral')
kelp = ('wakame', 'alaria', 'deep-sea tangle', 'macrocystis')

coral_kelp = (coral + kelp)

print(coral_kelp)

# max min methods for Tuples
more_numbers = (11.13, 34.87, 95.59, 82.49, 42.73, 11.12, 95.57)
print(max(more_numbers))

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

# Functions to Access Elements

dict.keys() #isolates keys
dict.values() #isolates values
dict.items() #returns items in a list format of (key, value) tuple pairs

# dictionary looping the values
for key, value in sammy.items():
    print(key, 'is the key for the value', value)
    #updating to a dictionary
    dictionary.update({key:value})


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

#make your own for loop
integers = []

for i in range(10):
   integers.append(i)

print(integers)

#nested for loops

list_of_lists = [['hammerhead', 'great white', 'dogfish'],[0, 1, 2],[9.9, 8.8, 7.7]]

for list in list_of_lists:
    for item in list:
        print(item)

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
# CONTINUE: Goes to the top of the closest enclosing loop skips it .
# PASS: Does nothing at all or disrigard the condition.

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

#Constructor Method

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
    pi = 3.14 ###class variable

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

### more exples with constructor
class Shark:
    def __init__(self, name):
        self.name = name

    def swim(self):
        print(self.name + " is swimming.")

    def be_awesome(self):
        print(self.name + " is being awesome.")


def main():
    # Set name of Shark object
    sammy = Shark("Sammy")
    sammy.swim()
    sammy.be_awesome()

if __name__ == "__main__":
    main()

### working with more than 1 object
class Shark:
    def __init__(self, name):
        self.name = name

    def swim(self):
        print(self.name + " is swimming.")

    def be_awesome(self):
        print(self.name + " is being awesome.")

def main():
    sammy = Shark("Sammy")
    sammy.be_awesome()
    stevie = Shark("Stevie")
    stevie.swim()

if __name__ == "__main__":
  main()
# STRING FUNCTIONS
#method                 True if
str.isalnum()	String consists of only alphanumeric characters (no symbols)
str.isalpha()	String consists of only alphabetic characters (no symbols)
str.islower()	String’s alphabetic characters are all lower case
str.isnumeric()	String consists of only numeric characters
str.isspace()	String consists of only whitespace characters
str.istitle()	String is in title case
str.isupper()	String’s alphabetic characters are all upper case

# USING VARIABLES
glb_var = "global"

def var_function():
    lcl_var = "local"
    print(lcl_var)
    print(glb_var) #Print glb_var within function

var_function()

########
def new_shark():
    #Assign variable as global
    global shark
    shark = "Sammy"

#Call new_shark() function
new_shark()

#Print global variable shark
print(shark)



# USING STRING FORMATTERS
print("Sammy has {} balloons.".format(5))

#using variable with formatters
open_string = "Sammy loves {}."
print(open_string.format("open source"))

#using 2 formatters
new_open_string = "Sammy loves {} {}."                      #2 {} placeholders
print(new_open_string.format("open-source", "software"))    #Pass 2 strings into method, separated by a comma

# now with 4 formatters
sammy_string = "Sammy loves {} {}, and has {} {}."
print(sammy_string.format("open-source", "software", 5, "balloons"))

# changing the order of the string FORMATTERS by index
print("Sammy is a {3}, {2}, and {1} {0}!".format("happy", "smiling", "blue", "shark"))

# with a variable name of the formatters
print("Sammy the {0} {1} a {pr}.".format("shark", "made", pr = "pull request"))

# Format-Specification Mini-Language
# with F converions
print("Sammy ate {0:f} percent of a {1}!".format(75, "pizza"))


print("Sammy ate {0:.4f} percent of a pizza!".format(75.765367))
# floting the point 4 spaces

print("Sammy ate {0:.0f} percent of a pizza!".format(75.765367))
# setting it to 0

# add space of 7
print("Sammy has {0:7} red {1:16}!".format(5, "balloons"))

# align left & center
print("Sammy has {0:<4} red {1:^16}!".format(5, "balloons"))

# fomatters with VARIABLES
sammy = "Sammy has {} balloons today!"
nBalloons = 8
print(sammy.format(nBalloons))

# Unary Arithmetic Operations
i = 3.3
print(-i) #result is -3.3

# DIVMOD does the rimendir and the
divmod(985.5,115.25)
#result (8.0, 63.5)

985.5 // 115.25
# 8
985.5 % 115.25
# 63..

# POW (power of **)
hours = 24
total_bacteria = pow(2,hours)

print(total_bacteria)

# SUM return sum of .. and it will work with tuple and dictionaries
# it also take two arguments so
some_floats = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]
print(sum(some_floats))

# LIST COMPRIHENTION
    # take a string and turns it into a list
shark_letters = [letter for letter in 'shark']
print(shark_letters)

    # this is how it would be done with a for loop to achive the same result
shark_letters = []

for letter in 'shark':
    shark_letters.append(letter)

print(shark_letters)

# Using Conditionals with List Comprehensions
fish_tuple = ('blowfish', 'clownfish', 'catfish', 'octopus')

fish_list = [fish for fish in fish_tuple if fish != 'octopus']
print(fish_list)

# Nested Loops in a List Comprehension
    # for each loop nested
my_list = []

for x in [20, 40, 60]:
    for y in [2, 4, 6]:
        my_list.append(x * y)

print(my_list)
    # nested loop as a Comprehension

my_list = [x * y for x in [20, 40, 60] for y in [2, 4, 6]]
print(my_list)

### MODULES
from random import randint #random file/module then the function name
for i in range(10):
    print(randint(1, 25))

#Aliasing modules
import math as m

print(m.pi)
print(m.e)

# importing module in another directory
import sys
sys.path.append('/usr/sammy/')

import hello

# writing Conditionals Statements
if statement1:                  #outer if
    print("hello world")

    if nested_statement1:       #first nested if
        print("yes")

    elif nested_statement2:     #first nested elif
        print("maybe")

    else:                       #first nested else
        print("no")

elif statement2:                #outer elif
    print("hello galaxy")

    if nested_statement3:       #second nested if
        print("yes")

    elif nested_statement4:     #second nested elif
        print("maybe")

    else:                       #second nested else
        print("no")

else:                           #outer else
    statement("hello universe")
### MAIN
##Although in Python you can call the function at the bottom of your program and it will run (as we have done in the examples above), many programming languages (like C++ and Java) require a main function in order to execute. Including a main() function, though not required, can structure our Python programs in a logical way that puts the most important components of the program into one function. It can also make our programs easier for non-Python programmers to read.

def hello():
    print("Hello, World!")

def main():
    print("This is the main function.")
    hello()

main()

#using *args you can replace the arguments to something more flixible
def multiply(*args):
    z = 1
    for num in args:
        z *= num
    print(z)

multiply(4, 5)
multiply(10, 9)
multiply(2, 3, 4)
multiply(3, 5, 10, 6)

##using **kwargs
def print_kwargs(**kwargs):
        print(kwargs)

print_kwargs(kwargs_1="Shark", kwargs_2=4.5, kwargs_3=True)

###Classes
class Shark:
    def swim(self):
        print("The shark is swimming.")

    def be_awesome(self):
        print("The shark is being awesome.")


def main():
    sammy = Shark()
    sammy.swim()
    sammy.be_awesome()

if __name__ == "__main__":
    main()
###Class Inheritance

class Fish:
    def __init__(self, first_name, last_name="Fish",
                 skeleton="bone", eyelids=False):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim(self):
        print("The fish is swimming.")

    def swim_backwards(self):
        print("The fish can swim backwards.")
# class trout Inherates from the fish
class Trout(Fish):
    pass

terry = Trout("Terry")
print(terry.first_name + " " + terry.last_name)
print(terry.skeleton)
print(terry.eyelids)
terry.swim()
terry.swim_backwards()

# using super classes
class Trout(Fish):
    def __init__(self, water = "freshwater"):
        self.water = water
        super().__init__(self)

terry = Trout()

# Initialize first name
terry.first_name = "Terry"

# Use parent __init__() through super()
print(terry.first_name + " " + terry.last_name)
print(terry.eyelids)

# Use child __init__() override
print(terry.water)

# Use parent swim() method
terry.swim()

# over riding the parent fish in this case
class Shark(Fish):
    def __init__(self, first_name, last_name="Shark",
                 skeleton="cartilage", eyelids=True):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim_backwards(self):
        print("The shark cannot swim backwards, but can sink backwards.")

##multiple Inheritance or parents
class Coral:

    def community(self):
        print("Coral lives in a community.")


class Anemone:

    def protect_clownfish(self):
        print("The anemone is protecting the clownfish.")


class CoralReef(Coral, Anemone):
    pass

#Creating Polymorphic Classes
class Shark():
    def swim(self):
        print("The shark is swimming.")

    def swim_backwards(self):
        print("The shark cannot swim backwards, but can sink backwards.")

    def skeleton(self):
        print("The shark's skeleton is made of cartilage.")


class Clownfish():
    def swim(self):
        print("The clownfish is swimming.")

    def swim_backwards(self):
        print("The clownfish can swim backwards.")

    def skeleton(self):
        print("The clownfish's skeleton is made of bone.")


sammy = Shark()
sammy.skeleton()

casey = Clownfish()
casey.skeleton()
### debugging with
pbd

#to stop the code and access the variables
import code
code.interact(local=locals())

# banner can be set to a string, so that you can flag where the interpreter launches
# readfunc can be used as the InteractiveConsole.raw_input() method
# local will set the default namespace for the interpreter loop
# exitmsg can be set to a string to note where the interpreter ends
# With the local parameter, you can use, for example:
#
# local=locals() for a local namespace
# local=globals() for a global namespace
# local=dict(globals(), **locals()) to use both the global namespace and the present local namespace

#logg
import logging
logging.basicConfig(level=logging.DEBUG)


logging.basicConfig(filename="test.log", level=logging.DEBUG) #log them into a file
# Table of Logging Levels
# CRITICAL	50	logging.critical()	Show a serious error, the program may be unable to continue running
# ERROR	40	logging.error()	Show a more serious problem
# WARNING	30	logging.warning()	Indicate something unexpected happened, or could happen
# INFO	20	logging.info()	Confirm that things are working as expected
# DEBUG	10	logging.debug()	Diagnose problems, show detailed information
