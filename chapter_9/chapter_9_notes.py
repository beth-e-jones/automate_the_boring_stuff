"""
Filepaths - the c:\ part of the path is the root folder
In windows, paths written usinng backslashes(\) but mac and linux use forward 
slashes (/)

If you want programmes to work on all operating systems you have to account for
this in your script. Can do so using path() function. Here, if you pass the
string values of individual file and folder names, path() will return a string
with a file path using the correct path separators
"""

from pathlib import path
Path('spam', 'bacon', 'eggs')


WindowsPath('spam/bacon/eggs')
str(Path('spam', 'bacon', 'eggs'))
'spam\\bacon\\eggs'

"""
Note that there are double backslashes because each backslash needs to be 
escaped by another backslash character.

Youu can also use path  objects with functions to join names form a list of 
file names to the end of a folder name e.g.,
"""
from pathlib import Path
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
print(Path(r'C:\Users\Al', filename))
C:\Users\Al\accounts.txt
C:\Users\Al\details.csv
C:\Users\Al\invite.docx

"""Using the / operator to join paths
We can use the + operator to add paths together or modify a path object after
we used path() to create it
"""
from pathlib import Path
Path('spam') / 'bacon' / 'eggs'

WindowsPath('spam/bacon/eggs')
Path('spam') / Path('bacon/eggs')

WindowsPath('spam/bacon/eggs')

Path('spam') / Path('bacon', 'eggs')
WindowsPath('spam/bacon/eggs')

"""Here the pathlib module solves problems with deciding what slash to use by
using / to join paths """
homeFolder = Path('C:/Users/Al')
subFolder = Path('spam')
homeFolder / subFolder
WindowsPath('C:/Users/Al/spam')
str(homeFolder / subFolder)
'C:\\Users\\Al\\spam'

"""But the thing to know when using / is that one of the first two values
must be a Path object, otherwise you get an error.


cwd = current working directory
path.cwd() will print the working directory as a string
os.chdir(NEW_DIRECTORY) will change the directory

All users also have a folder for their own files called a home directory
path.home() will print this

Absolute vs relative file paths
Absolute (begins with root folder)
Relative (relative to programmes current working directory)

Single dot . means "in this directory"
Double dot .. means "the parent folder"

Can create new folders with os.makedirs() if we give the new filepath e.g.,
os.makedirs('C:\\delicious\\walnut\\waffles')

Path.cwd().is_absolute() provides a Boolean outcome on whether path is absolute
to get an absolute path from relative path, use Path.cwd() / in front of the
relative path

"""