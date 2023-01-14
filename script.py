money = float(input("Введите сумму вклада: "))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

deposit = list(map(lambda num: round(num / 100 * money), per_cent.values()))

print("Максимальная сумма, которую вы можете заработать — %d" % max(deposit))
