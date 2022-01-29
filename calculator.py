def add(n,m):
    return n+m
def subtract(n,m):
    return n+m
def multiply(n,m):
    return n*m
def divide(n,m):
    return n/m
def percentage(n,m):
    return n%m
n = int(input("What is the 1st number:"))
x = input("Pick an operation:\n+\n-\n*\n/\n%\n")
m = int(input("Enter the second number: "))
if x == "+":
    print(add(n,m))
elif x == "-":
    print(subtract(n,m))
elif x == "*":
    print(multiply(n,m))
elif x == "/":
    print(divide(n,m))
elif x == "%":
    print(percentage(n,m))