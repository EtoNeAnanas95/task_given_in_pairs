from os import system as command
from msvcrt import kbhit, getch
from time import sleep
from dataclasses import dataclass



@dataclass(slots=True, frozen=True)
class Character:
    name: str
    surname: str
    middle_name: str
def add_to_inventory(inventory: set, item: str) -> None:
    inventory.update(item)

    show_message(f"Добавлен предмет \"{item}\" в Ваш инвентарь.", clear=False, spacing=True, tooltip=False, wait_for_key=False)

def choose_option(
        label: str,
        options: list,
        clear: bool = True,
        is_string: bool = True
) -> int:
    if clear is True:
        command("cls")

    print()
    print()
    print(label)

    for index, option in enumerate(options):
        print(f"{index + 1}. {option}")

    while True:
        try:
            print()
            choice = int(input(f"Выберите от 1 - {len(options)}: "))
            if 1 <= choice <= len(options):
                if is_string is True:
                    return options[choice - 1]
                else:
                    return choice - 1
            else:
                print(f"Неправильный выбор. Выберите пожалуйста между 1 и {len(options)}")
        except ValueError:
            print("Неправильный ввод. Введите пожалуйста число.")

def type(text: str, name: str = None) -> None:
    for letter in text:
        if kbhit():
            key = getch()

            if key == b'\r':
                command("cls")

                if name:
                    show_name(name)

                print(text)

            break

        print(letter, end="", flush=True)
        sleep(0.025)
def show_name(name: str) -> None:
    print(f"[{name}]: ", end="")
def show_tooltip() -> None:
    print("Для того чтобы пропустить анимацию нажмите ENTER")
    print()
def wait_for_any_key() -> None:
    print()
    print()
    print('Нажмите любую клавишу, чтобы продолжить', end='', flush=True)
    getch()
def show_message(
        text: str,
        name: str = None,
        clear: bool = True,
        spacing: bool = False,
        tooltip: bool = True,
        wait_for_key: bool = False
) -> None:
    if clear is True:
        command("cls")

    if name:
        show_name(name)

    if tooltip is True:
        show_tooltip()

    type(text)

    if wait_for_key is True:
        wait_for_any_key()

    if spacing is True:
        print()

    if clear is True:
        sleep(0.3)
        command("cls")

def menu(reader) -> None:
    while True:
        print("Выберите действие:\n1. Сохранения\n2. Начать Заново\n")
        try:
            menu = int(input())
            if menu == 1 or menu == 2:
                break
        except ValueError: print("Данные введены не верно")
        match menu:
            case 1:
                command("cls")
                line_number = 0
                row_count = 0
                for row in reader:
                    line_number += 1
                    row_count += 1
                    name = row[0]
                    game_moment = row[1]
                    print(f"{line_number}. Имя: {name}, момент игры: {game_moment}")
                try:
                    while True:
                        row_index = int(input("Выберите сохранение: "))
                        if row_index <= row_count and row_index >= 1:
                            for index, row in enumerate(reader):
                                if index == row_index:
                                    print(row)
                except ValueError: print("Данные введены не верно")
            case 2:
              pass