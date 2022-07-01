# 7 nuber program
#  1,3,A,RAJ,AADI,$,A,E,I,O,U,323,4,8,10,100,1000,
import math


#
# print(m)
# didgi = []
# alp = []
# for i in m:
#     if i.isdigit():
#         didgi.append(i)
#     else:
#         alp.append(i)
# print(didgi)
# print(alp)
#
#
# def perfect_square(n):
#     return (n ** 0.5) % int(n ** 0.5) == 0
#
# li = [1, 3, 323, 4, 8, 10, 100, 1000]
# def show_square(li):
#     square_list = []
#     for data in li:
#         if perfect_square(data):
#             square_list.append(data)
#     print(f"Square in the {square_list}")
#
# show_square(li)
#
#
# def perfectCube(li):
#     cube = 0;
#     li_cube=[]
#     for i in li:
#         cube = i * i * i;
#         if (cube == li):
#             li_cube.append(cube)
#         else:
#            pass
#     print(li_cube)
# perfectCube(li)
#
#
# def latter(alp):
#     if alp[0] == alp[-1]:
#         print("start and end are same")
#     else:
#         print('Start and end not same')
#
#
# latter(name)
#
#
# def vovels(name):
#     vove = []
#     for i in name:
#         if i in 'aeiou':
#             vove.append(i)
#         else:
#             pass
#     vove.sort()
#     print('voveles', set(vove))
#
#
# vovels(name)
#
#
# def special_char():
#     sp=[]
#     for i in name:
#         if i in '!@#$%&*^':
#             sp.append(i)
#         else:
#             pass
#     print('special char:',sp)
# special_char()
#
# #
# def seq(alp):
#     char = input("Search charter")
#     i = 0
#     count = 0
#
#     while (i < len(alp)):
#         if (alp[i] == char):
#             count = count + 1
#         i = i + 1
#
#     print("char of {} is Occurred {} ".format(char, count))
# seq(alp)
#




name = str(input('Enter value').lower())

m = name.split(",")
print(m)
li=[]
for i in m:
    if len(i)>1:
        li.append(i)
        for j in li:
            print(j)
    print(li)
