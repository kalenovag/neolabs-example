# class Jets:
#
#     def __init__(self, name, country):
#         self.name = name
#         self.origin = country
#
# first_item = Jets("F16", "USA")
#
# a = first_item.name
# print(a)
#
# class Jets:
#     model = None
#     country = 0
#
#     def __init__(self, name, country):
#         self.name = name
#         self.origin = country
#
#
# first_item =Jets("F16", "USA")
# second_item= Jets("SU33", "Turkey")
# tird_item= Jets("AJS56", "Russia")
# fourth_item= Jets("TU154", "Russia")
# fifth_item= Jets("Mirage100", "France")
#
# first_army=[first_item, second_item, tird_item, fourth_item, fifth_item]
# for element in first_army:
#     print(element.name)



class Jets:
    model = None
    country = 0

#     def __init__(self, name, country, quantity):
#         self.name = name
#         self.origin = country
#         self.quantity = quantity
#
#
# first_item = Jets("F14", "Turkey", 87)
# second_item = Jets("Mirage100", "Korea", 35)
# total = first_item.quantity + second_item.quantity
# print(total)

# class Nobel:
#     def __init__(self, category, year, winner):
#         self.category = category
#         self.year = year
#         self.winner = winner
#
#     def __str__(self):
#         return f"категорияЖ {self.category}, год: {self.year}, победитель: {self.winner}"
#
#
# np7=Nobel ("Peace", 2023, "Kalenova Gulzari")
# # print(np7.category, np7.year, np7.winner)
# print(np7)

# class Myfunc:
#
#     def fifth(x):
#         return x ** 5
#
# ans = Myfunc.fifth(3 )
# print(ans)

class Doctor:
    def __init__(self, name, qualification ):
        self.name = name
        self.qualfication = qualification


    def cure(self):
        print("лечит")

    def __str__(self):
        return f"имя: {self.name}, квалификация: {self.qualfication}, лечит: {self.cure()}"

man= Doctor (" Mahmudov Islam", "Кардиолог", "Сердечно-сосудистые болезни": )
print(man)

