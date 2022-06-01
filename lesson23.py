# try:
#     1/0 #данное деление покажет ошибку
#     print("hey")
# except: #поймаем ошибку,чтобы код не останавливался
#     print("на ноль делить нельзя")

# my_list = [1, "text", 0]
# for element in my_list:
#     try:
#         print(1/element)
#     except ZeroDivisionError:
#         print("Ошибка деления на ноль")
#     except TypeError:
#         print("ошибка разных типов")
#     except:
#         print("любая другая ошибка")

# try:
#     num = int(input("введите позитивное число: "))
#
#     if num > 0:
#         print("все правильно, число: ", num)
#     else:
#         raise ValueError(num, "непозитивное число")
# except ValueError as ve:
#     print(ve)

# #создайте функцию, которая принимает три числа и выдает самое большое
# def max_num(a,b,c):
#     print(max(a,b,c))
# max_num(1,2,3)

# mylist = ['jordan', 'airmax', 'runair']
# print(len(str(398)))


# x = 156
# num_x = len(str(x))
# print(num_x)



