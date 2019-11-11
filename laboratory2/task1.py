from validators import *

print("Германчук Аліна Вікторівна \nЛабораторна робота №1 \nВаріант 7 \nЗнаходження кількості негатвних чисел\n")
a=float(input("Введіть число a "))
b=float(input("Введіть число b "))
c=float(input("Введіть число c "))
if a<0:
        x=1
else:
        x=0
if b<0:
        y=1
else:
        y=0
if c<0:
        z=1
else:
        z=0
s=x+y+z
print("Кількість негативних чисел -", str(s))
