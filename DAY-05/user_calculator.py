import sys

def addition ( a, b):
    add = a + b
    return add

def subtraction ( x, y):
    sub = x - y
    return sub

def multiflication ( c , q):
    mul = c * q
    return mul

print (addition ( 2, 3))

a = float (sys.argv[1])
operation = sys.argv[2]
b = float (sys.argv[3])

if operation == "add":
    output = addition( a, b)
elif operation == "sub":
    output = subtraction( a, b)
elif operation == "mull":
    output = multiflication(a, b)
else:
    output = "invalid operation"


print(output)

