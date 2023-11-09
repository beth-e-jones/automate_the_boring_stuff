"""
Regular expressions allow us to specify a pattern of text to search for e.g.,
415-555-1234 is a US phone number but 4,155,551,234 is not
Can check this manually using python by checking a string of numbers is exactly
12 characters, each secion contains only numeric characters, and the pattern is
correct with hyphens between area codes. However, this is a long winded way of
doing this. it's also an issue because if you wanted to find a phone number
within a larger string, you'd have to add more code to spot the number pattern
(see the example)

It's easier to find patterns with regular expressions - called regexes for 
short. These are descriptions of any pattern of text e.g., \d is a digit
so \d\d\d-\d\d\d-\d\d\d\d would represent a US phone number, but ({3}) will
tell Python to replicate that pattern 3 times, so  \d{3}-\d{3}-\d{4} will also
do the job.

CREATING REGEX OBJECT
import re # re is the package for regex

to pass a string value representing the regex to re.compile() will return a 
regex pattern object. 

To make an object that matches a phonr number pattern:
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

searching involves searching for the specific object in a string passed to the
regex using search(). It will return a Match Object if the pattern is found in
the string, so will return None if the pattern isn't there.

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())
Phone number found: 415-555-4242

mo is a generic name for match objects. 


Steps to reg ex matching:
While there are several steps to using regular expressions in Python, each step
is fairly simple.

1. Import the regex module with import re.
2. Create a Regex object with the re.compile() function. (Remember to use a 
raw string.)
3. Pass the string you want to search into the Regex object's search() method. 
This returns a Match object.
4. Call the Match object's group() method to return a string of the actual 
matched text.

Ways to pattern match using regular expressions
Group with parentheses - will make a group you can return

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
mo.group(1)
'415'
mo.group(2)
'555-4242'
mo.group(0)
'415-555-4242'
mo.group()
'415-555-4242'

To retrieve all groups at once, use groups() method and note the plural

When using things like brackets in the pattern you're searching for, you'll 
need an escape character e.g., 
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')

Characters that would need escape characters
.  ^  $  *  +  ?  {  }  [  ]  \  |  (  )

Escape like this
\.  \^  \$  \*  \+  \?  \{  \}  \[  \]  \\  \|  \(  \)


Using pipes to match multiple groups
| is a pipe character = | (I've seen it used for OR before, and it's the same
here for reg ex)

SO if we wanted to search a string for either Batman or Tina fay, we'd use this
heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')

But beware as it will bring back the first instance of either as the match 
object

For stuff with the same prefix, you can use the pipe here with brackets
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')

Optional matching using ? character
batRegex = re.compile(r'Bat(wo)?man') 
will find batman and bat woman

THe ? character will match text with 0 or 1 instances of that character
for 0, 1, or multiple instances then use * instead
batRegex = re.compile(r'Bat(wo)*man')
will pick up Batman, Batwoman, or batwowowowowoman

The + character here means "match one or more"
batRegex = re.compile(r'Bat(wo)+man')

Matching repetitions with braces
regex = re.compile(ha{3}) will search for hahaha
You can specify a range too e.g.,
(Ha){3,5} will match 'HaHaHa', 'HaHaHaHa', and 'HaHaHaHaHa'.
and leave numbers out for it to be unbounded

Greedy and non greedy matching
Regular expressions are greedy by dafault, meaning that they will match the 
longest string psosible. THe non greedy form of the braces, which matches the 
shortest string possible has a closing } followed by a ?

Examples of greedy and non greedy matching
>>> greedyHaRegex = re.compile(r'(Ha){3,5}')
>>> mo1 = greedyHaRegex.search('HaHaHaHaHa')
>>> mo1.group()
'HaHaHaHaHa'

>>> nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
>>> mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
>>> mo2.group()
'HaHaHa'

??? Beware
Note that the question mark can have two meanings in regular expressions: 
declaring a non-greedy match or 
flagging an optional group. 

These meanings are entirely unrelated.

Findall() methods
Search() will return a match object of the first matched text in the string 
being searched, but findall() will return the strings
If the regular expression has groups, findall() will return a list of tuples

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
[('415', '555', '9999'), ('212', '555', '0000')]


Shorthand character class

Represents

\d  Any numeric digit from 0 to 9.

\D  Any character that is not a numeric digit from 0 to 9.

\w  Any letter, numeric digit, or the underscore character. (Think of this as 
    matching “word” characters.)

\W  Any character that is not a letter, numeric digit, or the underscore character.

\s  Any space, tab, or newline character. (Think of this as matching “space” characters.)

\S  Any character that is not a space, tab, or newline.

Making your own character classes
You can define your own classes using square brackets e.g., [aeiouAEIOU] will
match any lower or upper case vowels

[a-zA-Z0-9] will match all lower case letters, upper case letters, and numbers

Caret and dollar signs
^ = match must occur at beginning of searched text
$ = match must occur at the end of the text

beginsWithHello = re.compile(r'^Hello')
beginsWithHello.search('Hello, world!')

. = wildcard character, will match any character except a new line e.g.,
>>> atRegex = re.compile(r'.at')
>>> atRegex.findall('The cat in the hat sat on the flat mat.')
['cat', 'hat', 'sat', 'lat', 'mat']

.* = will match everything and anything e.g.,
>>> nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
>>> mo = nameRegex.search('First Name: Al Last Name: Sweigart')
>>> mo.group(1)
'Al'
>>> mo.group(2)
'Sweigart'

Summary of regex symbols
The ? matches zero or one of the preceding group.
The * matches zero or more of the preceding group.
The + matches one or more of the preceding group.
The {n} matches exactly n of the preceding group.
The {n,} matches n or more of the preceding group.
The {,m} matches 0 to m of the preceding group.
The {n,m} matches at least n and at most m of the preceding group.
{n,m}? or *? or +? performs a non-greedy match of the preceding group.
^spam means the string must begin with spam.
spam$ means the string must end with spam.
The . matches any character, except newline characters.
\d, \w, and \s match a digit, word, or space character, respectively.
\D, \W, and \S match anything except a digit, word, or space character, respectively.
[abc] matches any character between the brackets (such as a, b, or c).
[^abc] matches any character that isn't between the brackets.

Case insensitive matching
becasue regular expressions match text exactly, we need to consider how to 
manage case insensitive matching
To manage this, put re.IGNORECASE or re.I as the second argument in 
re.compile() to accept matches with all cases

Substituting example
>>> namesRegex = re.compile(r'Agent \w+')
>>> namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
'CENSORED gave the secret documents to CENSORED.'


"""