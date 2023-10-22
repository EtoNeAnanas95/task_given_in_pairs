import os

from actions import *
from saves import choose_save, save_inventory, save_character, Save, load_inventory


def new_character() -> Character:
    inventory = []

    command("cls")
    character = Character(
        name=choose_option("Выберите имя:", names),
        surname=choose_option("Выберите фамилию:", surnames),
        middle_name=choose_option("Выберите отчество:", middle_names),
        username=input("Введите имя своего пользователя:"),
        inventory=inventory,
        action="introduction"
    )

    show_message(text=f"""
    Ваше имя: {character.name}
    Ваше фамилия: {character.surname}
    Ваше отчество: {character.middle_name}
          """, spacing=True, wait_for_key=True)

    return character


def new_game(character: Character) -> None:
    # Новая игра это по факту загрузка с action_one, но чтобы было понятнее я решил сделать отдельную функцию
    match Action_one(character):
        case 0:
            match Action_two(character):
                case 0:
                    Action_teaTime(character)
                case 1:
                    Action_homicide(character)
        case 1:
            match Action_three(character):
                case 0:
                    match Action_friend(character):
                        case 0:
                            Action_six(character)
                        case 1:
                            Action_five(character)
                case 1:
                    Action_three_alt(character)


def game_from_save(save: Save, character: Character) -> None:
    # Получаем action с которого надо загрузить игру из save полученного ранее в методе game
    action = save.action

    # Словарь, где ключ это action с которого мы будем загружать, а значение это функция, которая будет запущена
    actions = {
        "introduction": start_from_action_one,
        "beginning": start_from_action_one,
        "action_one": start_from_action_one,
        "action_two": start_from_action_two,
        "action_three": start_from_action_three,
        "action_teatime": Action_teaTime,
        "action_homicide": Action_homicide,
        "action_six": Action_six,
        "action_five": Action_five,
        "action_three_alt": Action_three_alt,
        "action_friend": start_from_action_friend,
    }

    # Выбираем по ключу значение из actions и запускаем его с аргументом character, чтобы сохранять в него наш последний action
    actions[action](character)


def game():
    # Запускаем выбор действия
    chosen = choose_option("Выберите действие: ", ["Начать игру заново", "Загрузить сохранение"], clear=True, is_string=False)

    match chosen:
        # Загрузить нового персонажа
        case 0:
            # Создает нового персонажа
            character = new_character()

            # Запускаем игру
            new_game(character)

            # После окончания игры сохраняем персонажа и инвентарь
            save_character(character)
            save_inventory(character)

        # Загрузить из сохранения
        case 1:
            # Если существует файл с сейвами, то загружаем с них
            if os.path.exists("saves.csv"):
                # Пользователь выбирает с какого пользователя и сохранения ему загрузиться, что эта функция это и возвращает
                user, save = choose_save()
                # Загружаем инвентарь из inventory.json, аргументами передаем username выбраного пользователя и имя выбраного персонажа из сейва (в виде массива, так будет проще сравнивать просто)
                inventory = load_inventory(user.username, [save.surname, save.name, save.middle_name])

                # Создаем нового персонажа
                character = Character(
                    name=save.name,
                    surname=save.surname,
                    middle_name=save.middle_name,
                    inventory=inventory,
                    username=user.username,
                    action=save.action
                )

                # Запускаем игру из сохранения
                game_from_save(save, character)
            # Было выбрано загрузить с сохранений, но их нет, поэтому создает нового персонажа и начинаем игру заново
            else:
                # Создает нового персонажа
                character = new_character()

                # Запускаем игру
                new_game(character)

            # После окончания игры сохраняем персонажа и инвентарь
            save_character(character)
            save_inventory(character)
