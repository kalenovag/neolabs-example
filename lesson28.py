# class Cat:
#     def __init__(self,name, cat_type):
#         self.name = name
#         self.cat_type = cat_type
#     def speak(selfs):
#         print("Meow Meow")
#     def sleep(self):
#         print("Zzzzzz")
#     def __str__(self):
#         return f"name: {self.name}, type: {self.cat_type}"
# cat1 = Cat("Baby", "British")
# print(cat1)
# cat1.speak()
# cat1.sleep()
#
# # пример 1 наследования
# class Person:
#     def walk(self):
#         print("человек ходит")
#
# class Doctor(Person):
#     def cure(self):
#         print("Доктор лечит")
#
# doctor1 = Doctor()
# doctor1.walk()
# doctor1.cure()




# #наследование от нескольких классов
# class Predator:
#     def hunt(self):
#         print("hunting")
#
# class Wolf:
#     def howl(self):
#         print("Woooooouuuuu")
#
# class Dog(Predator, Wolf):
#     pass
# dog1 = Dog()
# dog1.howl()
# dog1.hunt()


class Bird:
    def __init__(self,name):
        self.name = name
    def fly(self):
        print("bird is fly")
# class Penguin(Bird):
#     def __init__(self,name):
#         super().__init__(name)
#     def fly(self): #overriding
#         print("penguin is not fly")
#     def swim(self): #extending
#         print("swim fast")
# pepe = Penguin("pepe")
# print(pepe.name)
# pepe.fly()
# pepe.swim()



# class Jets:
#     def __init__(self,name,country,  engine, seat, speed):
#         self.type = "Jet"
#         self.area = "air"
#         self.name = name
#         self.origin = country
#         self.engine = engine
#         self.seat = seat
#         self.speed = speed
#
# class F14(Jets):
#
#     def __init__(self):
#         self.name='F14'
#         self.origin='USA'
#         self.engine=2
#         self.seat=120
#         self.speed=500
#
# a=F14()
# print(a.name)
# print(a.origin)
# print(a.engine, a.seat, a.speed)




# class AJS37(Jets):
#     def __init__(self):
#         self.name = 'AJS37'
#         self.origin= "Sweedom"
#
# b=AJS37()
# print(b.name,b.origin)

class Feline:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def play(self):
        print("can play")
    def  drink(self):
        print("drink milk")

class Hause_cat(Feline):
    def __init__(self,name,color):
        super().__init__(name,color)
    def sleep(self):
        print("always sleep")
    def drink(self):
        print("do not drink  milk")
cat1=Hause_cat('Kitty', 'white')
print(cat1.name,cat1.color)
cat1.sleep()
cat1.drink()
cat1.play()



