def sum_digits(number):
    sum = 0
    while number > 0:
        buffer = number % 10
        sum += buffer
        number //= 10
    return sum

try:
    number = int(input("Введите число: "))
    sum = sum_digits(number)
    print(f"Сумма цифр числа {number} равна {sum}")
except ValueError:
    print("Лол, чел, введи нормальные данные")