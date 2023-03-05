num1 = float(input("Enter the 1st number: "))
operator = input("Enter an operator like... (+ - * /): ")
num2 = float(input("Enter the 2nd number: "))


if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif num2 == 0:
    print("Thats satanic")
    exit()
elif operator == "/":
    result = num1 / num2
else:
    print(f"{operator} is not a valid operator")
    exit()

print(round(result, 3))