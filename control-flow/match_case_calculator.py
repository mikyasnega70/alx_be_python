num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
operations = input("Choose the operation (+, -, *, /):")

match operations:
    case '+':
        result = num1 + num2
        print(f"the result is {result}.")
    case '-':
        result = num1 - num2
        print(f"the result is {result}.")
    case '*':
        result = num1 * num2
        print(f"the result is {result}.")
    case '/':
        if num2 == 0:
            print("Cannot divide by zero.")
        result = num1 / num2
        print(f"the result is {result}.")
