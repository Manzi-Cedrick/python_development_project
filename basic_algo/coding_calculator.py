def addTwoNumbers(x, y):
    return x + y
def subtractTwoNumbers(x, y):
    return x - y
def multiplyTwoNumbers(x, y):
    return x * y
def divideTwoNumbers(x, y):
    return x / y
def moduloTwoNumbers(x, y):
    return x % y
input1 = int(input('Enter first number: '))
input2 = int(input('Enter second number: '))
print('Select operation.')
print('1.Add')
print('2.Subtract')
print('3.Multiply')
print('4.Divide')
print('5.Modulo')
choice = input('Enter choice(1/2/3/4/5): ')
if choice == '1':
    print(input1, "+", input2, "=", addTwoNumbers(input1, input2))
elif choice == '2':
    print(input1, "-", input2, "=", subtractTwoNumbers(input1, input2))
elif choice == '3':
    print(input1, "*", input2, "=", multiplyTwoNumbers(input1, input2))
elif choice == '4':
    print(input1, "/", input2, "=", divideTwoNumbers(input1, input2))
elif choice == '5':
    print(input1, "%", input2, "=", moduloTwoNumbers(input1, input2))
else:
    print("Invalid input")