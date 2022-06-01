# my_dict = {} #создание словаря
# print(type(my_dict))
#
# student = {"name": "Kalen",
#            "age": 123,
#            "hobbies": ["reading", "swimming", "cooking"],
#            "favorites music": ["hello", "fall again", "crazy in love"]}
# # print(*student["hobbies"], sep= ", ")

# for key, value in student.items():
#     if type(value) == list:
#         print(key, ":", *value)
#     else:
#         print(key, ":", value)


# my_dict = {"country": "Kyrgyzstan",
#            "capital": "Bishkek",
#            "cities": ["Bishkek", "Talas", "Karakol"]}
# # del my_dict["capital"] #удаляет навсегда
# # print(my_dict)
# # value = my_dict.pop("country") #удаляет из словаря и сохраняет в переменной
# # print(value)
# # key_value = my_dict.popitem()
# # print(key_value)
#
# my_dict["capital"] = "naryn"
# my_dict["region"] = "Central Asia"
# my_dict["cities"].append("Osh")
# print(my_dict)


#
# books = {}
# for elem in range(2):
#     key = input("введите ключ: ")
#     value = input("введите значение: ")
#     books[key] = value
# print(books)

# for item in books.items():
#     print(*item, sep = ":")

books = {"title": "little prince",
         "author": "Antoine de Sent-Exupery",
         "year": 1943}
user = int(input("введите колличество попыток: "))
for element in range(user):
    operation = input("удалить или добавить (app/del): ")
    if operation == "del":
        key = input("введите какой ключ удалить: ")
        del books[key]
    elif operation == "app":
        key = input("введите какой ключ добавить: ")
        value = input("введите какое значение добавить: ")
        books[key] = value
        print(books)
    else:
        print("ввод неверен, попытка сгорает")
