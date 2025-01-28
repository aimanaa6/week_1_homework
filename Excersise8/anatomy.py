# hash bang - shebang - this is a file path - #! signifies
#!/usr/bin/python

# Example Python script
# sys — System-specific parameters and functions - number of commands given to script
# sys is a module and module is the container for code - the actual script

# making the code in the sys file (aka module available to my anatomy.py script) sys is a built in module STANDARD library - we have not created it
import sys
# argv is part of the sys module
# Argument = len (number of items in a sequence)
# Len - gives us the number of arguments
# argc = argument_count
argument_count = len(sys.argv)
# string operand and one integer operand - cannot concat (str function)
print("Number of arguments " + str(argument_count))
# If value is more than one, 'too many args' will be printed' - a conditional statement
if argument_count > 1:
    print('Too many args')
# where is the variable whose value is a string 'World'
else:
    where='World'
    #this is the print function doing concatenation (gluing strings together)
    # we are passing 2 arguments - passing a literal string
    # "Hello" is the zeroth argument to the print function
    # the where variable is the 1st argument
    print("Hello", where)
    # print function is doing stelath concatenation - gluing things together
    print("zero", "one" , "two")
# argv = argument list
# simple concatenation '+'
# conc = string + string
# file name is already passed and is the zeroth argument, can add anything to the below and it will come up when run
print('Goodbye from ' + sys.argv[0])
print('one', 'two', 'three')
# sep = seperator
print('one', 'two', 'three', sep="/")
# argument positions
# print(sys.argv[8])  - outside scope as there is no position 9 due to count starting at 0 - run in Terminal for additional arguments
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])
print(sys.argv[4])
print(sys.argv[7])