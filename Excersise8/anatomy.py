#!/usr/bin/python
# Example Python Script
import sys

argument_count = len(sys.argv)
print(argument_count)
print("Number of arguments " + str(argument_count))

if argument_count > 1:
    print('Too many args')
    print(sys.argv[1])
    print(sys.argv[2])
    print(sys.argv[3])
    print(sys.argv[4])

else:
    where = 'World'
    print("Hello", where)

print('Goodbye from ' + sys.argv[0])
print('Goodbye from',sys.argv[0])
print('one', 'two', 'three')
print('one', 'two', 'three' , sep="Pooja")