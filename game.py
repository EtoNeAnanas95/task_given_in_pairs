from os import system as command
from Defs import *
from messages import *
from actions import *

def character() -> Character:
    command("cls")
    character = Character(
        name=choose_option("Выберите имя:", names),
        surname=choose_option("Выберите фамилию:", surnames),
        middle_name=choose_option("Выберите отчество:", middle_names)
    )
    show_message(text=f"""
    Ваше имя: {character.name}
    Ваше фамилия: {character.surname}
    Ваше отчество: {character.middle_name}
          """, spacing=True, wait_for_key=True)
def game(character: Character):
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