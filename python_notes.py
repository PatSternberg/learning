Coding cheatsheet

Lingo
sequence - a Python object class which includes strings, as well as lists, tuples and range objects
Dotfiles - a hidden file, since they are listed as .[filename] in the terminal
Commit - an instance of version controlled directory created with git
Git repo - a ‘Git repository’
Drill - a tightly focused and repetitive exercise designed to help a student become familiar with the basic building blocks of programming
REPL - ‘Read Evaluate Print Loop’ - means that the program will run, show the result, then loop back so you can add more code
concatenate - to join two strings together
assign - to store a value in a variable
f-string - a Python term for a string containing interpolation data and formed by formatting it  f’ { } ’  including content in { } inside it
Operand - one of the inputs of an operation. Operands are acted on by operators
Left-associative order - means to execute something, e.g. methods, in order from left to right (assuming no complications such as parentheses)
index - the position of an element in an object (e.g. a character in a string)
Zero indexing - the practice / functionality of a first index being index [0] (ie not [1])
whitespace dependent - a quality of a programming language where whitespace confers actual information in a particular context, rather than just being for the ease of the reader - e.g. in Python an indent of four spaces shows a line is part of a new block, whereas in another language this might be expressed by { } or do and end
Loop variable / index variable - a variable indicating the value in a for loop, commonly i for index is used but it can be anything
Refactoring - improving code that already works
Mutate / modify in place - Modifies the original value, rather than returned a separate new modified value
Scope - where a variable can be used e.g. a variable defined by a constructor method for a class can be used within that class
Command line
pwd - print which directory in right now
cd - change directory (include .. to go up one directory to parent)
ls - list visible items in directory
ls -A - list all visible and hidden files in a directory
ls -l – list visible items with extended information about each file
ls -lA / ls -Al / ls -l -A - list all visible and hidden files in a directory with extended information about each file
touch [filename] - updates the timestamp for a file with the [filename], or creates a file with that [filename] if none exists
mkdir [DirName] - creates a directory with the name [DirName]
rmdir [DirName] - removes a directory with the name [DirName]
rm [FileName] - removes a file with [FileName]
rm -r [FileName] - remove file/directory [FileName] and all files inside it
cp [Filename] [NewFilename] - makes a copy of Filename with NewFilename
mv [file location][fileName] [new file location][FinalFileName] - move the file at the specified location to the new location and rename the file with a new file name if desired
echo “[Text]” > [fileName] - changes the files contents to be the Text, or creates a new file with fileName containing the Text if none exists
man [command] - gives details about a command related options

Git
git init - initialise git in the directory for version control
git add [fileName] adds the named file as a file to the staging area for the next commit
git restore [fileName] discard changes to fileName since the last commit, or remove it from staging if it has been added there
git commit -m ‘[commitName]’ creates a commit containing the files in the staging area with the name CommitName
git log - show list of all commits
git remote -v - list any remotes set up for the git repo
git remote add [remoteName] [address] - add a remote with the name [remoteName] to the current git repo linked to the gitHub repo specified in [address] - convention is to name it ‘origin’ if working with multiple devs pushing to a single gitHub repo
git push -u [remoteName] [branchName] - push and save these settings as default for push the current gitRepo branch across the remote called remoteName (-u saves as default)
git pull [remoteName] [branchName] pull the repo info from gitHub to the local directory
git clone [address] - clone the repository at address and add it to the current one

Python
Syntax
f’ { } ‘ - creates a string with the content included between { } (e.g. a variable) interpolated into it. This is called an f-string
def [function name]: - define a new function
[ (start-index) : (stop-index) : (step-index) ] - this is the standard Python slice notation. The stop index is not inclusive - the last element in the slice will be the one before the stop-index value
== operator which returns true if both sides of the operation are equal
!= operator which returns true if both sides of the operation are not equal
newlist = [expression for item in iterable if condition == True] - list comprehension
<dict_name> = {<new_key>:<new_value> for <item> in <iterable>} - dictionary comprehension
lambda - used to create temporary functions with a single argument and the function name lambda, syntax is: lambda: argument, function
Functions
len(‘[string]’) - returns the length of [string]
class [className]() - defines a new class
str() - convert data to string
int() convert data to int
type() - takes anything as an argument and returns its data type
print() - takes anything as an argument and prints it to the terminal
abs() - takes a number as an argument and always returns a positive value
range(start_at, stop_before, step) - returns a range data type, beginning at start_at and ending right before stop_before
any(x in y for z in aa) - returns true if any one of x (from y) is a z in aa
Methods
[data].upper() / [data].lower() - upper or lower cases the string in ‘[data]’
capitalize() - capitalizes the first letter of a string
lower() - lower cases the whole string
isascii() - returns true if everything is ascii characters (?)
isalpha() - returns true if everything is an alphabet letter
title() - title caps the whole string (e.g. This Is Title Caps)
strip() - removes whitespace at the beginning and end of a string
swapcase() - swaps the case of each character in a string (upper / lower)
round(x, y) - rounds a float x to a number of decimals y
import [module name] - import a module for new functions (module must be installed)
math.ceil(x) - round up x, uses the math module
math.floor(x) - round down x, uses the math module
x.replace(y,z) - replace y with z in x
x.append() - add the element to a list x
items()
clear() - removes all elements from a list
reverse() - reverses the order of items in a list
pop(i) - returns the item at the position i, if specified, defaults to last item (-1)
index(item) - returns the index of the item if it is present in the list
sort() - sorts the list numerically / alphabetically
keys() - returns a list of the keys in a dictionary
values() - returns a list of the values in a dictionary
get(key) - returns only the pair value for the assigned key
items() - returns each key and the corresponding value(s) in a dictionary
pop(key) - removes the listed key from the dictionary
clear() - removes all keys and values from the dictionary
setdefault(key, default) - complicated one, the default is optional, returns the value of the key if it is present, ‘None’ if it is not present and no default was set, and the default if the key isn’t present but the default was set
def __init__([self]) - within a class, defines an instance function to execute when a new instance is created - often called ‘constructor method’
[dict].update() - combine two dictionaries ie a key-value pair with key-value pairs from another dictionary
join() - connect all elements in a list
x.remove(y) - remove element y from a list x
filter(x, y) runs through y and returns every value which is true for x
.update() - add a key-value pair to a dictionary

# ++ DEBUGGING ++
# == ERRORS ==

raise [Exception / TypeError / etc.]('Error message here') - prints the error message if the exception is raised
# |EXAMPLE|
x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")

# == PYTEST ==

pytest.raises(e.g. Exception) - used to test with pytest that an error is raised without exiting the program
# |EXAMPLE|
def test_present_unwrap_error():
    present = Present()
    with pytest.raises(Exception) as new_error:
        present.unwrap()
    error_message = str(new_error.value)
    assert error_message == 'No contents have been wrapped.'


Math module

Datetime module