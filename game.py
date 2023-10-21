from actions import *
import os
from saves import choose_save, save_inventory, save_character, Save, load_inventory

SAVE_FILE_PATH = os.path.join(os.getcwd(), "saves.csv")

def new_character() -> Character:
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


def game_from_save(save: Save, character: Character) -> None:
    print(character)

def game():
    if os.path.exists("saves.csv"):
        user, save = choose_save()
        inventory = load_inventory(user.username, [save.surname, save.name, save.middle_name])

        character = Character(
            name=save.name,
            surname=save.surname,
            middle_name=save.middle_name,
            inventory=inventory,
            username=user.username,
            action=save.action
        )

        game_from_save(save, character)
    else:
        character = new_character()
        new_game(character)

    save_character(character)
    save_inventory(character)


