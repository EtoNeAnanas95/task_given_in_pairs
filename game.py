from actions import *
import os
import csv

SAVE_FILE_PATH = os.path.join(os.getcwd(), "save.csv")

def character() -> Character:
    inventory = set()

    command("cls")
    character = Character(
        name=choose_option("Выберите имя:", names),
        surname=choose_option("Выберите фамилию:", surnames),
        middle_name=choose_option("Выберите отчество:", middle_names),
        username=input("Введите имя своего пользователя:"),
        inventory=inventory
    )

    show_message(text=f"""
    Ваше имя: {character.name}
    Ваше фамилия: {character.surname}
    Ваше отчество: {character.middle_name}
          """, spacing=True, wait_for_key=True)


def new_game(c: Character) -> None:
    match Action_one(c):
        case 0:
            match Action_two():
                case 0:
                    Action_teaTime()
                case 1:
                    Action_homicide()
        case 1:
            match Action_three():
                case 0:
                    match Action_friend(c):
                        case 0:
                            Action_six(c.inventory)
                        case 1:
                            Action_five(c.inventory)
                case 1:
                    Action_three_alt()


def game_from_save() -> None:
    with open(..., mode="r") as file:
        reader = csv.reader(file)
        menu(reader)


def game():
    if os.path.exists("save.csv"):
        game_from_save()
    else:
        new_game(character())
