def is_even(number):
    if number % 2 == 0:
        return True
    else: return False


try:
    number = float(input("Введите число: "))
    status = is_even(number)
    print(status)
except ValueError:
    print("Введите нормальные данные")
