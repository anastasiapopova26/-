'''
 Площадь и объем
Напишите программу, которая будет запрашивать у пользователя радиус и сохранять его в
переменной r. После этого она должна вычислить площадь круга с заданным радиусом и
объем шара с тем же радиусом. Используйте в своих вычислениях константу pi из модуля
math.
'''
import math as m
r = float(input("Ввудите радиус - "))
print('площадь круга:', m.pi * (r**2))
print('Объем шара:', m.pi * (r**3) * (4/3))