from all_the_defs import *
from collections import Counter
print("Для выхода нажмите 6")
while True:
    try:
        menu = int(input("Введите номер задания"))
        match menu:
            case 1:
                question_first()
            case 2:
                question_second()
            case 3:
                question_thrid()
            case 4:
                question_fourth()
            case 5:
                question_sixth()
            case 6:
                break
    except ValueError: print("Данные введены не верно")