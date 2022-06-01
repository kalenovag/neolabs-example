 # #test
# num = int(input("введите число: "))
# exception = (1, 2, 3, 5)
# if num in exception:
#     print("простое")
# elif num%2!=0 and num%3!=0 and num%5!=0:
#     print("простое")
# else:
#     print("не простое") #первое задание по тесту.
#
#
# def add(num1, num2):
#     print(num1 + num2)
#
# def sub(num1, num2):
#     print(num1 - num2)
#
# def multi(num1, num2):
#     print(num1 * num2)
#
# def div(num1, num2):
#     print(num1/num2)
#
# def deg(num1, num2):
#     print(num1 ** num2)
#
# def ost(num1, num2):
#     print(num1 % num2)
#
# def calculate():
#    num1 = float(input("введите первое число: "))
#    num2 = float(input("введите второе число: "))
#    operations = ["plus", "minus", "multi", "ost", "deg"]
#    oper = input("введите команду: ")
#    while oper not in operations:
#     oper = input("введите команду: ")
#
#    if oper == "plus":
#     add(num1, num2)
#    elif oper == "minus":
#     sub(num1, num2)
#    elif oper == "multi":
#     multi(num1, num2)
#    elif oper == "ost":
#     ost(num1, num2)
#    elif oper == "deg":
#     deg(num1, num2)
#
# while True: #цикл калкулятора
#     calculate()
#     again = input("повторить? (yes/no)")
#     if again == "yes":
#         calculate()
#     else:
#         break


def week (day):
    if day == 1:
        print("monday")
    elif day == 2:
        print("Tuesday")
    elif day == 3:
        print("Wednesday")
    elif day == 4:
        print("Thursday")
    elif day == 5:
        print("freee day")
    else:
        print("такого дня нет! ")






