def add(a, b):
    return a+b
def subtract(a, b):
    return a-b
def multiply(a, b):
    return a*b
def divide(a, b):
    return a/b

a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))
operator = (input("enter an operator: "))

if operator == "+":
    print(f"Answer is: {add(a, b)}")
elif operator == "-":
    print(f"Answer is: {subtract(a, b)}")
elif operator == "*":
    print(f"Answer is: {multiply(a, b)}")
elif operator == "/":
    print(f"Answer is: {divide(a, b)}")
else:
    print("invalid operator")

    
        
      

   
