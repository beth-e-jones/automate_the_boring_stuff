"""
Input validation checks values entered by users using input() are formatted
correctly. Important to avoid issues or vulnerabilities e.g., inputting a neg 
amount from withdraw_from_account could end up with balance being added

Can use loops or raise errors to pick up these issues and be limited in how we
ask for input e.g., 
try:
    age = int(age) 
to be sure age is an integer

The PyInputPlus Module
Contains functions similar to input() for a few different types of data, and 
will prompt users for refortmating input if it is incorrect.

Pyinputplus isn't part of the standard library so needs installing via pip
and importing at the top of python files

Different functions for inputs in pyinputplus
inputStr() = like standard input but can pass a custom validation function in
inputNum() = ensures user enters a number and returns an int or float 
inputChoice = ensures user picks one of pre-selected choices
inputMenu() = offers menu with number or letter options
inputDatetime()  = requires a date and time input
inputYesNo() = limits input to yes or no
inputBool() =takes a “True” or “False” response and returns  Boolean value
inputEmail() = limits input to valid email address
inputFilepath() = limits input to Ensures the user enters a valid file path/
                    filename, and can check that a file with that name exists
inputPassword()  = displays *s while user types to avoid visible sensitive info

Can combine this function with min, max, greaterThan, lessThan keywords to 
specify a range of valid values as arguments for the functions

Blank input isn't allowed until blank argument=True

Default is to keep asking for user input forever, but we can limit to a certain
number of tries or a set period of time from the first run using the limit
and timeout keyword

example
>>> import pyinputplus as pyip
>>> response = pyip.inputNum(limit=2)
blah
'blah' is not a number.
Enter num: number
'number' is not a number.
Traceback (most recent call last):
    --snip--
pyinputplus.RetryLimitException
>>> response = pyip.inputNum(timeout=10)
42 (entered after 10 seconds of waiting)
Traceback (most recent call last):
    --snip--
pyinputplus.TimeoutException


You can allow and block regesex using the allowRegexes and blockRegexes keyword
arguments respectively. THis will decide what the function considers valid 
e.g. allowing roman numbers
import pyinputplus as pyip
>>> response = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])

or you can block certain inputs using regexes e.g.,
>>> response = pyip.inputNum(blockRegexes=[r'[02468]$'])

Passing a custom validation function to inputCustom()
example
>>> import pyinputplus as pyip
>>> def addsUpToTen(numbers):
...   numbersList = list(numbers)
...   for i, digit in enumerate(numbersList):
...     numbersList[i] = int(digit)
...   if sum(numbersList) != 10:
...     raise Exception('The digits must add up to 10, not %s.' %
(sum(numbersList)))
...   return int(numbers) # Return an int form of numbers.
...
>>> response = pyip.inputCustom(addsUpToTen) # No parentheses after
addsUpToTen here.
123
The digits must add up to 10, not 6.
1235
The digits must add up to 10, not 11.
1234
>>> response # inputStr() returned an int, not a string.
1234
>>> response = pyip.inputCustom(addsUpToTen)
hello
invalid literal for int() with base 10: 'h'
55
>>> response

"""