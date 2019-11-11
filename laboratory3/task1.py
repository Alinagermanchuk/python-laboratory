print("Германчук Аліна Вікторівна \nЛабораторна робота №3 \nВаріант 7 \nЗамінити перші 3 символи слів на *\n")
First_str = str(input("Введіть рядок: "))
words = First_str.split()
New_list = []
for i in range(0, len(words)):
     if len(words[i]) < 3:
         print ("Рядок занадто малий. Введіть повторно рядок, де довжина слова більша від 3")
     else:
        n = str(("***")+ words[i][3:])
        New_list.append(n)
print(str(New_list)[1:-1])
