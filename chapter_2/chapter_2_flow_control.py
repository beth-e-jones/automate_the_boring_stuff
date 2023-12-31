""""
Flow control:
Flow control statements tell Python what to do under which conditions

Booleans - True and False
An integer or floating-point value will always be unequal to a string value
e.g., 42 == "42" will be False

= is an assignment
== asks whether 2 values are the same as eachother

Boolean operators are:
and
not
or

and are used to compare Boolean values. 
Python looks at them in the order 
not, then and, then or

*And* and *or* are binary operators, and the *and* provides a True output if 
both are true. Otherwise, it'll output False. 

The *not* operator works with just one Boolean value/expression
which makes it a unary operator.


Flow control 
Flow control statements start with a condition, then followed by a clause
Condition = can always evaluate down to a Boolean value of True or False
A flow control statement makes a decision based on whether condition is True or
False. 

Lines of code can be grouped into blocks. Blocks have 3 rules:
Blocks begin when indentation changes, and end when indentation goes back to zero. 
Blocks can contain other blocks.

Types of flow control statements
if statement (if, then condition, colon, indented action to take)
else statement (else, then a colon, then the indented action to take)
elif (elif, a condition that can evaluate to True/False, colon, indented action)
while statement (while, then a condition - true/false, colon, action)


Infinite loops:
Ctrl + C will terminate a programme immediately as a good way of getting out 
of infinite loop, or interrupt programme in VS Code. 

Break statements:
A shrotcut to break a while loop early. If Python gets to a break statement, 
it'll exist the while loop. Just needs to contain the break keyword.

Continue statements:
Also used inside loops - once the programme reaches a continue statement, it 
jumps back to the start of a loop and re-evaluates the loop's condition.

Truthy and Falsey variables:
Essentially true and false booleans
WHen used in conditions, 0, 0.0 and "" are considered False, everything else 
is true. 

sys.exit() will stop a function before the last line, if a certain condition
is met e.g.,

import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')
    
    But note that you have to import sys first
"""
