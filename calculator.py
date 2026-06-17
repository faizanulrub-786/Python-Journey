num1 = int(input("Write the first number:- "))
num2 = int(input("Write the second number:- "))
operator = input("Write the operator ")

if operator== '+':
    print(num1+num2)
elif operator== '-':
    print(num1-num2)
elif operator== '*':
    print(num1*num2)
elif operator== '/':
    print(num1/num2)
else:
    print("Invalid syntax")