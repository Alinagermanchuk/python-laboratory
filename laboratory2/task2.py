from validators import *

print("Германчук Аліна Вікторівна \nЛабораторна робота №2 \nВаріант 7 \nОбчислення добутку (x+i)\n")
n=int(input('Введіть n: '))
x=int(input('Введіть x: '))
product = x+1
for i in range(2, n+1):
        product *= (x+i)
print('Результат добутку (x+i) = ',product)
