sum = 0
try:
    num = int(input('Введите количество посетителей:\t'))
    if num < 1:
        raise ValueError()
except ValueError as e:
    print('Вы ввели неправильное число')
else:
    for i in range(num):
        try:
            age = int(input(f"Введите возраст {i + 1} посетителя\t"))
            if age > 100 or age <= 0:
                raise ValueError()
        except ValueError as error:
            print("Неправильный возраст")
        else:
            if 17 < age < 25:
                sum += 990
            if age > 24:
                sum += 1390

if num > 3:
    sum *= 0.9
print(f"Стоимость билетов для {num} посетителей составила {sum} рублей")
