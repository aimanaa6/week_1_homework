# Variable (var) is the value that is input in the prompt
var=input("Please enter a value: ")
# The variable will become uppercase using .upper to convert
print("Uppercase value", var.upper())
# len = the number of items of an object - this will calculate the number of characters in the var
print("Number of characters", len(var))
# .isdecimal() produces true/false depending on if any of the characters in the string are numerical
print("Only numerical characters?", var.isdecimal())