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
