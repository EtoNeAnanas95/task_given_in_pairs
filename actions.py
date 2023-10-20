from messages import *
from Defs import *

def Action_one(character) -> int:
    show_message(text=f"""
    Ваше имя: {character.name}
    Ваше фамилия: {character.surname}
    Ваше отчество: {character.middle_name}
          """, spacing=True, wait_for_key=True)

    show_message(introduction, wait_for_key=True)
    show_message(beginning.format(name=character.name), wait_for_key=True)

    show_message(action_one, clear=False, tooltip=False, wait_for_key=False)

    index = choose_option("Выберите действие:", action_one_options, clear=False, is_string=False)
    choice = action_one_options[index]

    show_message(f"Вы выбрали: {choice}", clear=True, spacing=True, tooltip=False)
    return index

def Action_two() -> int:
    show_message(action_two, clear=False, tooltip=False)

    index = choose_option("Выберите действие:", action_two_options, clear=False, is_string=False)
    choice = action_two_options[index]

    show_message(f"Вы выбрали: {choice}", clear=True, spacing=True, tooltip=False, wait_for_key=False)
    return index

def Action_teaTime() -> None:
    show_message(name="Отец", text=action_teatime_dad_phrase, clear=False, spacing=True, tooltip=False,
                 wait_for_key=False)
    show_message(action_teatime, clear=False, tooltip=False, wait_for_key=True)
    show_message(good_ending_message, clear=True, tooltip=True, wait_for_key=True)

def Action_homicide() -> None:
    show_message(action_homicide, clear=False, tooltip=False, wait_for_key=True)
    show_message(bad_ending_message, clear=True, tooltip=True, wait_for_key=True)

def Action_three() -> int:
    show_message(action_three, clear=False, tooltip=False)

    index = choose_option("Выберите действие:", action_three_options, clear=False, is_string=False, )
    choice = action_three_options[index]

    show_message(f"Вы выбрали: {choice}", clear=True, spacing=True, tooltip=False, wait_for_key=False)
    return index

def Action_friend(character) -> int:
    show_message(name="Колян", text=action_friend_phrase_one, clear=False, spacing=True, tooltip=False,
                 wait_for_key=False)
    show_message(name=character.name, text=action_friend_phrase_character, clear=False, spacing=True, tooltip=False,
                 wait_for_key=False)
    show_message(name="Колян", text=action_friend_phrase_two, clear=False, spacing=True, tooltip=False,
                 wait_for_key=False)

    show_message(action_five, clear=False, spacing=True, tooltip=False, wait_for_key=False)

    index = choose_option("Выберите действие:", action_five_options, clear=False, is_string=False)
    choice = action_five_options[index]

    show_message(f"Вы выбрали: {choice}", clear=True, spacing=True, tooltip=False)
    return index

def Action_six(inventory: set) -> None:
    add_to_inventory(inventory, item="Ключ")
    add_to_inventory(inventory, item="Записка")

    show_message(action_six, clear=False, tooltip=False, wait_for_key=True)

    show_message(good_ending_message, clear=True, tooltip=True, wait_for_key=True)

def Action_five(inventory: set) -> None:
    add_to_inventory(inventory, item="Травушка муравушка")

    show_message(action_five_alt, clear=False, tooltip=False, wait_for_key=True)
    show_message(bad_ending_message, clear=True, tooltip=True, wait_for_key=True)

def Action_three_alt() -> None:
    show_message(text=action_three_alt, clear=False, spacing=True, tooltip=False, wait_for_key=True)
    show_message(bad_ending_message, clear=True, tooltip=True, wait_for_key=True)