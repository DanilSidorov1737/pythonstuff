operation = input("Selection:\n 1: Add,\n 2: Sub,\n 3: Multi,\n 4: Div\n")
num1 = int(input("Enter a Number: "))
num2 = int(input("Enter a Number: "))


if operation == '1':
    answer = num1 + num2
    print(answer)

if operation == '2':
    answer = num1 - num2
    print(answer)

if operation == '3':
    answer = num1 * num2
    print(answer)

if operation == '4':
    answer = num1 / num2
    print(answer)
