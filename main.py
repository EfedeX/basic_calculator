import time

from utils.dividir import dividir
from utils.multiplicacion import multiplicar
from utils.sumar import sumar
from utils.suma_avanzada import sumar_n_elementos
from utils.resta import restar


flag = True
while flag:
    print("What kind of operation would you like to do?")
    print(f"{'*'*20}")
    print("Divide two numbers: press 1")
    print("Multiply two numbers: press 2")
    print("Substract two numbers: press 3")
    print("Sum two numbers: press 4")
    print("Sum n amount of numbers: press 5")
    try:
        operation = int(input("Operation: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        break
    if operation > 5 or operation < 1:
        print("Invalid input. Please enter an operation between 1 and 5.")
        break
    if operation == 1:
        num1 = float(input("You selected division. Enter first digit: "))
        num2 = float(input("Enter second digit: "))
        print("The result of the division 'first digit / second digit' is: ", dividir(num1, num2))
    if operation == 2:
        num1 = float(input("You selected multiplication. Enter first digit: "))
        num2 = float(input("Enter second digit: "))
        print("The result of the product of 'first digit * second digit' is: ", multiplicar(num1, num2))
    if operation == 3:
        num1 = float(input("You selected subtraction. Enter first digit: "))
        num2 = float(input("Enter second digit: "))
        print("The result of the substraction 'first digit - second digit' is: ", restar(num1, num2))
    if operation == 4:
        num1 = float(input("You selected sum. Enter first digit: "))
        num2 = float(input("Enter second digit: "))
        print("The result of the division 'first digit + second digit' is: ", sumar(num1, num2))
    if operation == 5:
        nums_string = input("You selected sum n amount of number. Enter digits separeted by spaces: ")
        nums = list(map(float, nums_string.split()))
        print(f"The result of the sum of {len(nums)} elemnts is: ", sumar_n_elementos(nums))
    flag = bool(input("Continue? 0: No, 1: Yes"))
    time.sleep(0.5)