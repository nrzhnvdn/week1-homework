#1
# list: ordered, changeable, allow duplicates
# tuple: ordered, unchangeable, allow duplicates
# set: unordered, unchangeable, do not allow duplicates
# dict: ordered, changeable, do not allow duplicates
# thislist = ["apple", "banana", "cherry"]
# print(len(thislist)) 
# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)
# thistuple = ("apple", "banana", "cherry")
# print(thistuple)
# thistuple = ("apple", "banana", "cherry", "apple", "cherry")
# print(thistuple[1])
# thisset = {"apple", "banana", "cherry"}
# print(thisset)
# thisset = {"apple", "banana", "cherry", "apple"}

# print(thisset)
# myset = {"apple", "banana", "cherry"}
# print(type(myset))
# thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
# print(thisset)
# thisset = {"apple", "banana", "cherry"}

# for x in thisset:
#   print(x)
# thisset = {"apple", "banana", "cherry"}

# thisset.discard("banana")

# # print(thisset)
# thisset = {"apple", "banana", "cherry"}

# for x in thisset:
#   print(x)`
# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}

# set3 = set1.union(set2)
# print(set3)
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(thisdict)
#2
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# # print(thislist)
# a = ["HELLO", "I", "AM", "WRITING", "CODE"]
# a.sort(key = str.lower)
# print(a)
# #2.1
# step = 0
# distance = 10
# while step < distance:
#   step += 3
#   print("step number:", step)
# print("reached", step)
#3
# mylist=["Danagul", "Alibek", "Beka", "Zhenya"]
# mylist.append("programmers")
# print(mylist)
#4
# file = open("test.txt", "w")
# def my_func(name):
#     file.write(name)

# for x in range(1,1000):
#     my_func("I am developer\n")

#5
# a = [1,1,2,3,5,8,13,21,34,55,89]
# b = []
# for i in a:
#     if i < 5:
#         b.append(i)
# print('b = {}'.format(b))

#6
# a = {1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89}
# b = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
# a.symmetric_difference_update(b)
# print(a)

#7

# list1 = [2,3,4,7,237,2,2,4]
# for x in list1:
#     if x == 237:
#         break
#     elif x % 2 == 0:
#         print(x)

#8
# print('asdasdsdd! Asd lsdl!! sd ! Sd'.count('!'))

#9
# from random import random
# N = 10 
# arr = [0] * N
# for i in range(N):
#     arr[i] = int(random() * 100)
# print(arr)
# for i in range(N-1):
#     for j in range(i+1, N):
#         if arr[i] == arr[j]:
#             print("False")
#             quit()
# print("True")

#10
# import collections

# text = 'Напишите функцию, которая принимает текст и выводит два слова наиболее часто встречающееся и самое длинное'
# words = text.split()
# counter = collections.Counter(words)
# most_common, occurrences = counter.most_common()[0]

# longest = max(words, key=len)

# print(most_common, ",", longest)

#11
# from random import random

# n = random() * 900 + 100
# n = int(n)
# print(n)
# a = n // 100
# b = (n // 10) % 10
# c = n % 10
 
# print("Сумма: ", a+b+c)
# print("Произведение: ", a*b*c)

#12
# from random import random
# n = round(random() * 51)
# i = 1
# print("Компьютер загадал число. У вас 3 попыток")
# while i <= 3:
#     a = int(input(str(i) + '-я попытка: '))
#     if a > n:
#         print('Меньше')
#     elif a < n:
#         print('Больше')
#     else:
#         print('Вы угадали')
#         break
#     i += 1
# else:
#     print('Game over. Было загадано', n)

#13
# a = int(input())
# b = int(input())
# c = int(input())
# if a == b == c:
#     print(3)
# elif a == b or b == c or a == c:
#     print(2)
# else:
#     print(0)

#14
# a = input()
# b = a.split()
# c = '_'.join(b)  
# print(c)

#15
# def fill_list(m1, m2, amount, l):
#     from random import randint
#     for i in range(amount):
#         l.append(randint(m1, m2))
 
 
# def analysis(your_list, your_dict):
#     for i in your_list:
#         if i in your_dict:
#             your_dict[i] += 1
#         else:
#             your_dict[i] = 1
 
 
# list1 = []
# dict1 = {}
 
# minimum = int(input('Минимум: '))
# maximum = int(input('Максимум: '))
# quantity = int(input('Количество элементов: '))
 
# fill_list(minimum, maximum, quantity, list1)
# analysis(list1, dict1)
 
# for item in sorted(dict1):
#     print("'%d':%d" % (item, dict1[item]))

#16

# a = [2,3,4]
# print(a[0], a[1], a[2])


# def sum(list1):
#     b = 0
#     for i in list1:
#         b+=i
#     return b

# print(sum(a))


# def sum(list1):
#     b = 1
#     for i in list1:
#         b*=i
#     return b

# print(sum(a))

# def mult1(a):
#     b = 0
#     c = 0
#     while c < len(a):
#         b += a[c]
#         c += 1
#     return b

# print(mult1(a))

# def mult1(a):
#     b = 1
#     c = 0
#     while c < len(a):
#         b *= a[c]
#         c += 1
#     return b

# print(mult1(a))

#17
# a = input('a = ')
# b = input('b = ')
# # i = 0
# # l = 0
# # if len(a)<len(b):
# #     l = len(a)
# # else:
# #     l = len(b)

# # while l > i:
# #     if int(a[i])>int(b[i]):
# #         print(a+b)
# #         break

# #     elif int(a[i])<int(b[i]):
# #         print(b+a)
# #         break

# #     else:
# #         if len(a)>len(b):
# #             print(a+b)
# #             break
# #         elif len(a)<len(b):
# #             print(b+a)
# #             break
# #     i+=1

# if int(a+b)>int(b+a):
#     print(a+b)
# else:
#     print(b+a)

#18
# y = int(input("Введите год: "))
# if y % 4 != 0:
#     print("Не високосный")
# elif y % 100 == 0:
#     if y % 400 == 0:
#         print("Високосный")
#     else:
#         print("Не високосный")
# else:
#     print("Високосный")

#19
import os
for root, dirs, files in os.walk("."):  
    for filename in files:
        print(filename)



