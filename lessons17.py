#           0           1               2
# tuple1 = ("orange", [10, 20, 30], (12, 13, 14))
# num = tuple1[1]
# print(num[1])


# for elem in range(-10, 0):
#     print(elem)

# -10 -3 -2 -1 0 1 2 3




# sample_dict = {"physics": 80,
#                "math": 65,
#               "history":70
#                }
#
# values = sample_dict.values() # сохраняем значения
# print(min(values))


# print(sample_dict["math"])




# n = int(input("Введите число от 1 до 5 : "))
#
# if n > 9 or n < 1:
#     print("Еrrоr")
# else:
#     s = ''
#     for i in range(1, n + 1):
#         s += str(i)
#         print(s)



#  функции
# def info(): #обьявление
#     print("hiya") #
# info() #
#
# def greet(name): #один параметр
#     print(f"Добро пожаловать {name}!")
#     """Приветствует человека,чье имя указано"""
# greet("Gulzari") #один аргумент
# print(greet.__doc__) #dokumentiruet
#
# def add(num, num2): #параметры
#     print(num+ num2)
#
#
# add(5,6) #фргумент

# def test():
#     print('gulzari')
#
# test()

# def sub(num1, num2): #primer raznosti chisel
#     print(num1 - num2)

# sub(19, 6)

def square(side):
    print(side*side)

side = int(input("Введите число: "))
square(side)
