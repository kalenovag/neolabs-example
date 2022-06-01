# def info(name):
#     print(name)
# info("farrad")
#
# def info2(name):
#     return name
# print(info2("vika"))

#
# def adder(x,y,z):
#     print(x+y+z)
# adder(10,16,68)

# def adder(*nums):
#     summary = 0
#     for element in nums:
#         summary += element
#     print("сумма:", summary)
#
# adder(7,8,9) #неважно сколько аргументов,складывает числа

# def info(**data):
#     for key, value in data.items():
#         print(key, value)
#
# info(title = "detective", writer = "Kalen Gulzari", copy = 742964)
#
# my_dict = {"title": "Avengers"} #в словаре ключи надо ставить в ковычки
# print(my_dict)

# def students(*names): #вывод имен через аргс
#     for name in names:
#         print(name)
# students("Aidar", "Aidana", "Vikz")

# def students(): #вывод имен через инпут без аргументов
#     names = input("введите имена: ").split()
#     for element in names:
#         print(element)
#
# students()


#
# def greet(age, name = "user"):
#     print("welcome", name)
# greet(23, "peta paka")

#напишите функцию, которая принимает неизвестное количество чисел и выодит ти числа деленные на два

# def nums(*args):
#     for element in args: # для (какого-то числа- element) внутри кортежа (1,2,3,4)
#         print(element/2) # берем это число и делим на 2
# nums(1,2,3,4)

# def adder(*nums):
#     for element in nums:
#        if element % 2 == 0:
#            print(element)
#
# adder(6,8,4,9,5,7)

password = ["neo", "hey", "chek", "neolabs"]
secret = "neolabs"
for letter in password:
    if letter == secret:
        print("yeap")
    elif letter != secret:
        print("nope")

