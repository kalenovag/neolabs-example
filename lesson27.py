# class Parrot:
#
#     species = "bird"
#
#     def __init__(self, name, age): #атрибут обьекта, динамический
#         self.name = name
#         self.age = age
#
#
#
# blu = Parrot("Blu", 10)
# woo = Parrot("Woo", 15)
# print("Blu is a {}".format(blu.__class__.species))
# print("Woo is a {}".format(woo.__class__.species))
#
# print("{} is {} years old".format(blu.name, blu.age))
# print("{} is {} years old".format(woo.name, woo.age))


# class Bird:
#
#     def __init__(self):
#         print("Bird is ready")
#
#     def whoisThis(self):
#         print("Bird")
#
#     def swim(self):
#         print("Swim faster")

# class Penguin(Bird):
#
#     def __init__(self):
#         super().__init__()
#         print("Penguin is ready")
#
#     def whoisThis(self): #overriding (перезапись)
#         print("Penguin")
#
#     def run(self): #extending (расширение)
#         print("Run faster")
#
# peggy = Penguin()
# peggy.whoisThis()
# peggy.swim()
# peggy.run()




# class Phone:
#     def __init__(self):
#         self.__price = 900
#
#     def getPrice(self): # геттер выдает инфо
#         print(self.__price)
#
#     def setPrice(self, price): #сеттер изменяет инфо
#         self.__price = price

# Nokia = Phone()
# Nokia.setPrice(3000)
# Nokia.getPrice()

# class Person:
#     def __init__(self):
#         self.__name = "user"
#     def getName(self):
#         return  self.__name
#     def setName(self,name):
#         self.__name = name
#
#
# person1 = Person()
# print(person1.getName())
# person1.setName("Kalen")
# print(person1.getName())



class Dog:

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def speak(self):
        print("WOW")

    def __str__(self):
        return f"name: {self.name}, breed:{self.breed}"

description = Dog("Garik", "Bulldog")

a = description.name
print(a)
b = description.breed
print(b)

