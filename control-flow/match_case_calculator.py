#!/bin/python3

num1 = int (input("Enter the first number: "))
num2 = int (input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case '+':
        result = num1 + num2
        print(f"The result is {result}.")

    case '-':
        result = num1 - num2
        print(f"The result is {result}.")

    case '*':
        result = num1 * num2
        print(f"The result is {result}.")

    case '/':
        if num2 == 0:
            print("annot divide by zero.")
        else:
            result = num1 / num2
            print("The result is {result}.")

