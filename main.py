"""Задано список з цілих чисел. Напишіть функцію, яка
повертає суму всіх елементів цього списку. Напишіть код,
що демонструє роботу функції та показує суму елементів у
деяких списках."""

lst=[1,2,3,4,5]
def listochek(lst):
    return(sum(lst))
print(listochek(lst))

"""Напишіть функцію, яка приймає рядок та повертає
True, якщо рядок є паліндромом, та False в іншому випадку"""

def string1():
    str1=input("Введіть рядок: ")
    if str1[::-1]==str1[::]:
        return True
    elif str1[::-1]!=str1[::]:
        return False
print(string1())


""" Створіть функцію, яка приймає список рядків та повертає
список рядків, відсортованих за зростанням довжини."""


s=["63h14e44","jh5jtdfyt","kuildtj"]
def list(s):
    return sorted(s, key=len)
print(list(s))