def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2

num1 = (input("Enter first number: "))
operation = input("Enter operation (+, -, *, /): ")
num2 = (input("Enter second number: "))

result = calculator(operation, num1, num2)
print("Result:", result)