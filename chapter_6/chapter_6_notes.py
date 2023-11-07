"""
Lots of ways we can use strings, and lots of things we haven't covered yet

String literals - problem with using a ' in a string is that anything after
the apostrophe is mistaken for not inside the string. Manage this by using 
double quotation marks or an escape character (\ followed by the character 
e.g., \')

\' Single quote

\" Double quote

\t Tab

\n Newline (line break)

\\ Backslash

You can also use a raw string, which involves r before the string (like an f
string) and it knows that any symbols in there should be taken literally
print(r'That is Carol\'s cat.')

Can index and slice strings just like a list.
FOr in and not in, remember this is case sensitive

Putting strings in other strings    
So far we've done it with +, for example
"Hello, my name is ' + name + '. I am ' + str(age) + ' years old.'

We could use stirng interpolation, where % acts as a marker to replaced 
by values
'My name is %s. I am %s years old.' % (name, age)

We can also use f strings

USEFUL STRING METHODS
.upper() = returns new string where everything is upper case
.lower()= returns new string where everything is lower case
.isupper() = will return True if at least one upper case letter
.islower() =  will return True if at least one lower case letter
.isalpha() =  will return True if string only letters
.isalnum() =  will return True if string only letters and numbers
.isdecimal() =  will return True if string only numeric characters
.isspace() =  will return True if string only spaces, tabs and new lines
.istitle() =  will return True if string has first letter upper case
.startswith() = will return true if this is correct
.endswith() = will return true if this is correct

.join() = attaches list of strings together and returns a single, 
        concatenated string
.split() = separates single string and returns a list of strings. Can be 
        specific about where we split 

'MyABCnameABCisABCSimon'.split('ABC')
['My', 'name', 'is', 'Simon']

'My name is Simon'.split('m')
['My na', 'e is Si', 'on']

.partition() method - splits string into a text before and after a separator
string. Will create a tuple- before, after, and separator

JUSTIFYING STRINGS
arguments = total length, fill character (default " ")
.rjust() = justifying right based on argument for number of spaces
.ljust() = justifying left based on argument for number of spaces
.centre() = justifying centrally based on argument for number of spaces

STRIPPING WHITE SPACE
.lstrip() = strips white space from left
.rstrip() = strips white space from right
.strip() = strips white space from both ends

UNICODING
ord() = gets the code point of a one character string
chr() = gets hte one character string of a code point

pyperclip = option for copy and paste
given examples on putting in bullet poimns
"""
