operator = input("Enter a operator ( + - * / ) : ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))
result = 0

if operator == "+":
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
elif operator == "*":
    result = number1 * number2
elif operator == "/":
    result = number1 / number2
else:
    print("Error")