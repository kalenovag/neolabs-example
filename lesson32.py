# with open('lesson32.txt', 'w', encoding="utf-8") as file:
   # for i in range(1, 101):
   #     file.write(f"{i}\n")



# with open('kuzya.py', 'w', encoding="utf-8") as file:
#     file.write(f'''class F14:
#
#     def __init__(self):
#         self.name='F14'
#         self.origin='USA'
#         self.engine=2
#         self.seat=120
#         self.speed=500''')
#
# from kuzya import *
#
# a=F14()
# print(a.name)
# print(a.origin)
# print(a.engine, a.seat, a.speed)



with open('kuzya.py', 'r', encoding="utf-8") as file:
    user = input("введите текст: ")
    for word in file.read().split():
        if word in user:
            user = user.replace(word, "*"*len(word))
    print(user)


