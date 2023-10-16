from collections import Counter

def question_first():
    try:
        path_the_file = str(input("Введите путь до файла"))
            #"C:\\Users\\1\\Desktop\\grades.txt"
        try:
            with open(path_the_file, "r") as file:
                lines = file.readlines()
                line_count = len(lines)
                print(f"Количество строк в файле {line_count}")
        except FileNotFoundError:
            print("Файл не найден, возможно вы ввели не правльный путь")

    except ValueError: print("Данные введены не верно")

def question_second():
    try:
        path_the_file = str(input("Введите путь до файла"))
        # "C:\\Users\\1\\Desktop\\grades.txt"
        with open(path_the_file, "r") as file:
            passed_students = 0
            for line in file:
                data = line.strip().split()
                grades = list(map(int, data[1:]))
            if sum(grades) >= 65:
                passed_students += 1
        print(f"Сдало студентов: {passed_students}")
    except ValueError: print("Данные введены не верно")

def question_thrid():
    try:
        path_the_file = str(input("Введите путь до файла"))
        # "C:\\Users\\1\\Desktop\\words.txt"
        with open(path_the_file, "r", encoding="utf-8") as file:
            words = file.read().split()
            max_len = len(max(words, key=len))
            longest_words = [word for word in words if len(word) == max_len]
            for word in longest_words:
                print(word)
    except ValueError: print("Данные введены не верно")

def question_fourth():
    try:
        path_the_file = str(input("Введите путь до файла"))
        # "C:\\Users\\1\\Desktop\\words.txt"
        with open(path_the_file, "r", encoding="utf-8") as file:
            words = file.read().split()
            counter = Counter(words)
            most_common = counter.most_common(1)
            print(repr(most_common))

    except ValueError: print("Данные введены не верно")

def question_sixth():
    try:
        path_the_file1 = str(input("Введите путь до первого файла"))
        # "C:\\Users\\1\\Desktop\\words1.txt"
        path_the_file2 = str(input("Введите путь до второго файла"))
        # "C:\\Users\\1\\Desktop\\words2.txt"
        with open(path_the_file1, "r", encoding="utf-8") as file1, open(path_the_file2, "r", encoding="utf-8") as file2:
            lines1 = file1.readlines()
            lines2 = file2.readlines()
            for i, line in enumerate(lines1):
                if lines2[i] != line:
                    print(f"Линия {i + 1} отличается:")
                    print(f"в первом файле: {line.strip()}")
                    print(f"в втором файле: {lines2[i].strip()}")
    except ValueError: print("Данные введены не верно")
