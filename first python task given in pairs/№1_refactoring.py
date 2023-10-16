import math
from re import match

print("Для прекращение работы калькулятора, напишите слово (да)")
Cheker = "ответ убил"
print("1. сложение ")
print("2. вычитание ")
print("3. умножение ")
print("4. деление ")
print("5. возведение в степень ")
print("6. корень числа ")
print("7. факториал числа ")
print("8. синус числа ")
print("9. косинус числа ")
print("10. тангенс числа ")

# Сидят двое водку пьют. Подходит к ним мужик и спрашивает
# -Что отмечаем мужики?
# -Водку купили


def print_function():
    print("Ах маленький пернатый проказник, введи нормальные знечения))))")


def input_function1():
    try:
        print("Введите первое число")
        a = float(input())
        print("Введите второе число")
        b = float(input())
        return a, b

    except ValueError:
        print_function()

def input_function2():
    try:
        print("Введите первое число")
        a = float(input())
        print("Введите второе число")
        b = int(input())
        return a, b

    except ValueError:
        print_function()

try:
    c = int(input("выберите дейсвтие: "))
    while Cheker != "yes" and Cheker != "да" and Cheker != "yea" and Cheker != "lf":
        match c:
            case 1:
                a, b = input_function1()
                Q = a + b
                print("Ответ: ", a, ' + ', b, ' = ', Q)
                print("Завершить работу?")
                Cheker = str(input())
            case 2:
                a, b = input_function1()
                Q = a - b
                print("Ответ: ", a, ' - ', b, ' = ', Q)
                print("Завершить работу?")
                Cheker = str(input())
            case 3:
                a, b = input_function2()
                Q = a * b
                print("Ответ: ", a, ' * ', b, ' = ', Q)
                print("Завершить работу?")
                Cheker = str(input())
            case 4:
                a, b = input_function2()
                if b == 0:
                    print("Ах маленький пернатый проказник, на ноль делить нельзя))))")
                    print("Введи пожалуйста другой делитель")
                    break
                Q = a / b
                print("Ответ: ", a, ' / ', b, ' = ', Q)
                print("Завершить работу?")
                Cheker = str(input())
            case 5:
                a, b = input_function2()
                Q = a ** b
                print("Ответ ", Q)
                print("Завершить работу?")
                Cheker = str(input())
            case 6:
                try:
                    print("Введите первое число")
                    a = float(input())
                    Q = a ** 0.5
                    print("Ответ ", Q)
                    print("Завершить работу?")
                    Cheker = str(input())
                except ValueError:
                    print_function()
            case 7:
                try:
                    print("Введите первое число")
                    a = int(input())
                    from math import factorial
                    print("Ответ ", factorial(a))
                    print("Завершить работу?")
                    Cheker = str(input())
                except ValueError:
                    print_function()
            case 8:
                try:
                    print("Введите число")
                    a = int(input())
                    from math import sin
                    print("Ответ ", sin(a))
                    print("Завершить работу?")
                    Cheker = str(input())
                except ValueError:
                    print_function()
            case 9:
                try:
                    print("Введите число")
                    a = int(input())
                    from math import cos
                    print("Ответ ", cos(a))
                    print("Завершить работу?")
                    Cheker = str(input())
                except ValueError:
                    print_function()
            case 10:
                try:
                    print("Введите число")
                    a = int(input())
                    from math import tan
                    print("Ответ ", tan(a))
                    print("Завершить работу?")
                    Cheker = str(input())
                except ValueError:
                    print_function()
except ValueError:
    print_function()
    print()
    print("""У моей дочери сдохла собака, и, чтобы взбодрить ее,
я нашел и принес ей точно такую же. Она расплакалась
и спросила меня: Зачем мне две мертвые собаки?.""")
