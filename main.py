from game import *
import os
import csv

current_directory = os.getcwd()
file_path = os.path.join(current_directory, 'save.csv')

if os.path.exists(file_path):
    with open(file_path, mode="r") as file:
        reader = csv.reader(file)
        menu(reader)

else:
    with open("save.csv", "w", newline="") as file:
        writer = csv.writer(file)
    user_name = str(input("Введите имя пользователя: "))
    character = character()
    game_moment = game(character)


command("cls")
character = Character(
    name=choose_option("Выберите имя:", names),
    surname=choose_option("Выберите фамилию:", surnames),
    middle_name=choose_option("Выберите отчество:", middle_names)
)
inventory = set()

match Action_one(character):
    case 0:
        match Action_two():
            case 0:
               Action_teaTime()
            case 1:
                Action_homicide()
    case 1:
        match Action_three():
            case 0:
                match Action_friend(character):
                    case 0:
                        Action_six(inventory)
                    case 1:
                        Action_five(inventory)
            case 1:
                Action_three_alt()