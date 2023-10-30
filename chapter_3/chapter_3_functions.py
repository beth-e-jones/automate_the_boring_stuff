"""
Adding functions will help deduplicate code - will make programmes shorter and 
easier to read and update.

When calling functions like print() or len() you give them values, or arugments
in the brackets
e.g.,
def hello(name):
    print("Hello," + name)

hello("Alice")

The value stored in a parameter is forgotten when the function returns.

Define = Defining a function just means creating it

Call = putting in the functions name (as you've defined it), so it'll send python
execution to the top of the code for that function to run it

Pass = Giving the value (in brackets when you call a function) to the function 
to run

Argument = A value being given to a function call e.g., "Alice" being assigned
to name

Parameter = Variables with arguments assigned to them


Return values and return statements:
When you call a function e.g., len() and pass it an argument like "Hello", the 
function call evaluates it to the integer of 5. Value that the function call 
evaluates is the "return value" of the function.

When we make functions, you can specify what the return value should be by using
a return statement. This involves: 1. the return keyword, 2. the value or 
expression that the function should return.

None value:
Represents an absense of a value - typed with capital N
Useful when you want to store something that won't be confused for a real value
in a variable 
e.g. 
>>> spam = print('Hello!')
Hello!
>>> None == spam
True

Python will add None to the end of any function definition without a 
return statement, and this works in the same way that while or for loop implicitly
ends with a continue statement. If you use a return statement without a value,
None is returned. 


Keyword arguments and print(): 
Most arguments are identified by where they are in the function cell e.g., 
random.randint(1,10) will work but random.randint(10,1) won't because the lower
integer should be first. 

Keyword arguments are identified by the key word put before them in function
call. They are often used for optional parameters e.g., print() function has 
optional arguments for end and sep, to specify what should be printed at the end
of the argument and between arguments. 

When you pass multiple string values to print, it'll automatically get separated
with a space, but you can change the sep to make it different e.g.,
>>> print('cats', 'dogs', 'mice')
cats dogs mice

becomes 
>>> print('cats', 'dogs', 'mice', sep='')
catsdogsmice


Call stack - how python remembers where to return the execution
after each function is called. Python does this in the background.
When we call a functino, Python creates a "frame object" on top of a call stack
which remembers the line number of the original function call so python knows
where to go back to. 


Local and global scope:
Parameters and variables that are assigned in a function exist in that function's
"local scope". A variables assigned outside functions are said to exist in 
"global scope". Therefore, variables assigned in global and local scope are known
as global and local variables respectively. 

A global scope is created when the programme begins, and ends when it terminates.
Local scope is created when a function is called, and when the function returns
then the local scope is forgotten. 

This is important because code in global scope can't use local variables, but
local scope code can use global variables. you can also use the same name for 
different variables in different scopes which can cause confusion.

Local scopes can't use variables from other local scopes

If you need to modify a global variable from inside a function, use the global 
statement
e.g., a function where locally eggs = "spam"
can write global eggs

Exception handling:
At the moment, an error or exception will just crash Python. In the real world,
we want programme to detect and fix errors then carry on.

We can manage errors with try and except statements.
Code that might have an error  


"""