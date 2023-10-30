"""
Lists
List = values in an ordered sequence, separated using commas

Lists can contain other lists (so be lists of lists). We can index using 
multiple indexes, e.g., [0] [1] will return the second value in the first list

Remember negative indexes too! -1 is last index in a list
Can slice within list using [:]

can overwrite individual list values with list_name[index] = 
e.g., spam[1] = "aardvark"

Lists can be concatenated like strings, using +
e.g., 
[1, 2, 3] + ['A', 'B', 'C']
[1, 2, 3, 'A', 'B', 'C']

del listname[index] will delete items from a list
This will basically unassign, so if you use a variable after deleting it, you'll
get a name error as the cariable no longer exists

del is mainly used to delete values from lists

Multiple assignments - basically tuple unpacking lets you assign multiple
variables with values in a list in single line of code e.g.,
cat = ['fat', 'gray', 'loud']
size, color, disposition = cat

remember to iterate over length of a list, you need to do 
"in range(len(listname))"

e.g.,
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

Index 0 in supplies is: pens
Index 1 in supplies is: staplers
Index 2 in supplies is: flamethrowers
Index 3 in supplies is: binders

Can check what is in/not in a list using in and not in

Enumerate()
Great instead of using range(len(list))
On each iteration of a loop, enumerate will return 2 values: the index of item 
in the list, and the item itself e.g.,

supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' in supplies is: ' + item)
 
 

Indexing
Can find the index position of an item by using
list_name.index(item)

Appending and inserting won't give a new value as it's return value, and the 
return value is actually None so don't store the return as the new variable 
value

Methods are specific, can't append to strings ot insert to an integer 

Removing values from list with listname.remove(item) but if a value appears
multiple times, only first instance will be removed

Can reverse list with listname.reverse()


Mutable and immutable data types
Lists are mutable - can have items removed, added, or changed
Strings are immutable - fixed
Proper way to mutate a string is to slice and concatenate
e.g.
name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]


Tuples
Typed with parentheses, and are immutable in a way that lists are not.
Tuples can't be modified, appended, or removed

Can convert between two with list() and tuple() functions
"""