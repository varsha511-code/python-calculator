num1=float(input("enter first number:"))
num2=float(input("enter second number:"))
operation=input("choose operation(+,-,*,/):")
if operation=="+":
print(num1+num2)
elif operation=="-":
print(num1-num2)
elif operation=="*":
print(num1*num2)
elif operation=="/":
print(num1/num2)
else:
print("invalid operation")
