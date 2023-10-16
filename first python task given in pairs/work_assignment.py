from itertools import count

cheker = "ответ убил"
a = [1, 2, 3, 4, 5, 6, 6, 6]
b = [7, 8, 9, 10]

def function_1(numbers):
    b = sum(numbers)
    return b

def function_2(numbers):
    b = sorted(numbers)
    c = len(numbers)
    max = numbers[c-1]
    return max

def function_3(numbers):
    unique_set = set(numbers)
    unique_list = list(unique_set)
    return unique_list

def function_4(numbers_1, numbers_2):
    res = numbers_1 + numbers_2
    return res



while cheker != "да":
    print(f"Список {a}")
    print("""Выберите задачу: 
1. 
2.
3. 
4. 
5. """)
    menu = int(input())
    match menu:
        case 1:
            res = function_1(a)
            print("Сумма элеметнов списка ", res, "\n")
            cheker = str(input("Закончить?"))
        case 2:
            res = function_2(a)
            print(f"Наибольший элемент равен: {res} \n")
        case 3:
            res = function_3(a)
            print(f"уникальный лист {res} \n")
        case 4:
            res = function_4(a, b)
            print(f"совмещённый листик  {res} \n")
        case 5:
            res
