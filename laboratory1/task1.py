from validators import *

print("Германчук Аліна Вікторівна \nЛабораторна робота №1 \nВаріант 7 \nЗнаходження суми вкладу\n")
deposit = float(input("Введіть початковий вклад: "))
persent = float(input("Введіть відсоток "))
sum = deposit*(1 + persent/100)**5
if deposit < 0 or persent < 0:
    answer = "Вклад або відсоток не може бути від`ємним"
else:
    answer = "Сума вкладу через 5 років = " + str(round(sum,2))
print(answer)
