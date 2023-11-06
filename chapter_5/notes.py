"""
Dictionary is a mutable collection of values that use keys, and values. 
We can access values using keys, rather than index positions
e.g.,
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

myCat['size']
'fat'
'My cat has ' + myCat['color'] + ' fur.'
'My cat has gray fur.'

Keys(), values(), items() methods
The values returned using these methods are not true lists, they can't be
changed and you can't append. However, the data types can be used in for loops
e.g.,

spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print(v)
    
and loops can iterate over keys, or both values and keys e.g.,
for i in spam.items():
    print(i)

('color', 'red')
('age', 42)


If you want to use one of these methods with a true list, you have to pass the
list-like return into the list() function e.g.,
spam = {'color': 'red', 'age': 42}
spam.keys()

alternatively, you can use the multiple assignment trick on a for loop to assign
key and value to separate variables e.g.,
spam = {'color': 'red', 'age': 42}
for k, v in spam.items():
print('Key: ' + k + ' Value: ' + str(v))


If you want to check whether a key or value exists in dictionaries, you can 
just go "name" in listname.keys() or listname.values()

get() method
You can use this method if you don't want to have to check a key exists in a
dictionary before trying to access its value. Here, dictionaries using get() 
require 2 arguments. 1 is the key of the value you're trying to find, and a 
backup if the key doesn't exist. 
E.g., 
picnicItems = {'apples': 5, 'cups': 2}
'I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.'
'I am bringing 2 cups.'

'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.'
'I am bringing 0 eggs.'

Because eggs isn't in dictionary, it defaults to the alternate value offered 
in the argument

We can also setdefault() for when keys don't already have a value 
Can do it manually, like this 
spam = {'name': 'Pooka', 'age': 5}
if 'color' not in spam:
    spam['color'] = 'black'
    
or in a single line of code like this:
 spam.setdefault('color', 'black')
 

Pretty printing
If you import pprint module into programmes, you can use pprint() and pformat()
functions, that print things more neatly than the standard print() function.
Here, the output is cleaner, with keys sorted and one item per line.

Nested dictionaries and lists
You may find that you need dictionaries and/or lists to contain dictionaries
or lists themself e.g.,
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}


"""