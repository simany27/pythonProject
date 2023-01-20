count = int(input("Введите количество билетов: "))
summa = 0
for i in range(1,count+1):
    age = int(input(f"Введите возраст посетителя № {i}: "))
    if 18 <= age < 25:
        summa += 990
    elif age >= 25:
        summa += 1390
summa = round(summa * 0.9 if count > 3 else summa)
print(f"Сумма к оплате: {summa}")

