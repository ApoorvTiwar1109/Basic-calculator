print("What is the  basic operator (+, -, *, /) you want to use?")
op = input()
x = int(input("Enter first number:"))
y = int(input("Enter second number:"))
sum1 = (x + y)
difference1 = (x - y)
product1 = (x * y)
quotient1 = (x/y)
if op =="+":
    print(sum1)
elif op =="-":
    print(difference1)
elif op =="*":
    print(product1)
elif op =="/":
    print(quotient1)
else:
    print("Not supported.")