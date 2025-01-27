var = input("Please enter a value: ")
# print(var)
print(var.upper())
print(len(var))
if var.isdecimal():
    print('The input contains numeric characters')
else:
    print('The input does not contain numeric characters')